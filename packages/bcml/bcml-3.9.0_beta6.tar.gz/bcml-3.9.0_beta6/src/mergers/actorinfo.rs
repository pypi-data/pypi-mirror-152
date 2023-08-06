use crate::{util, Result, RustError};
use pyo3::{prelude::*, types::PyBytes};
use rayon::prelude::*;
use roead::{byml::{Byml, Hash}, yaz0::{compress, decompress}};
use std::{sync::Arc, collections::BTreeMap};

type ActorMap = BTreeMap<u32, Byml>;

lazy_static::lazy_static! {
    static ref STOCK_ACTORINFO: Arc<Result<ActorMap>> = {
        let load = || -> Result<ActorMap> {
            if let Byml::Hash(hash) = Byml::from_binary(&decompress(std::fs::read(
                util::get_game_file("Actor/ActorInfo.product.sbyml")?,
            )?)?)? {
                Ok(hash["Actors"]
                    .as_array()?
                    .iter()
                    .map(|actor| {
                        (
                            roead::aamp::hash_name(
                                actor.as_hash().unwrap()["name"]
                                    .as_string()
                                    .unwrap()),
                            actor.clone(),
                        )
                    })
                    .collect())
            } else {
                Err(RustError::BymlError(roead::byml::BymlError::TypeError))
            }
        };
        Arc::new(
            load()
        )
    };
}

pub fn actorinfo_mod(py: Python, parent: &PyModule) -> PyResult<()> {
    let actorinfo_module = PyModule::new(py, "actorinfo")?;
    actorinfo_module.add_wrapped(wrap_pyfunction!(diff_actorinfo))?;
    actorinfo_module.add_wrapped(wrap_pyfunction!(merge_actorinfo))?;
    parent.add_submodule(actorinfo_module)?;
    Ok(())
}

fn stock_actorinfo() -> Result<&'static ActorMap> {
    if let Ok(hash) = STOCK_ACTORINFO.as_ref().as_ref() {
        Ok(hash)
    } else {
        Err(RustError::BymlError(roead::byml::BymlError::TypeError))
    }
}

pub fn merge_actormap(base: &mut ActorMap, other: &ActorMap) {
    other.iter().for_each(|(k, v)| {
        if let Some(bv) = base.get_mut(k) {
            match (bv, v) {
                (roead::byml::Byml::Hash(bh), roead::byml::Byml::Hash(oh)) => {
                    util::merge_map(bh, oh, false);
                }
                _ => {
                    base.insert(*k, v.clone());
                }
            }
        } else {
            base.insert(*k, v.clone());
        }
    })
}

#[pyfunction]
fn diff_actorinfo(py: Python, actorinfo_path: String) -> PyResult<PyObject> {
    let diff = py.allow_threads(|| -> Result<Vec<u8>> {
        if let Byml::Hash(mod_actorinfo) =
            Byml::from_binary(&decompress(&std::fs::read(&actorinfo_path)?)?)?
        {
            let stock_actorinfo = stock_actorinfo()?;
            let diff: Hash = mod_actorinfo
                .get("Actors")
                .ok_or_else(|| anyhow::format_err!("Modded actor info missing Actors data"))?
                .as_array()?
                .par_iter()
                .filter_map(|actor| {
                    actor.as_hash().ok().and_then(|actor_hash| {
                        let name = actor_hash.get("name")?.as_string().ok()?;
                        let hash = roead::aamp::hash_name(name);
                        if !stock_actorinfo.contains_key(&hash) {
                            Some((hash.to_string(), actor.clone()))
                        } else if let Some(Byml::Hash(stock_actor)) = stock_actorinfo.get(&hash)
                            && stock_actor != actor_hash 
                        {
                            Some((
                                hash.to_string(),
                                Byml::Hash(actor_hash.iter().filter_map(|(k, v)| {
                                    (stock_actor.get(k) != Some(v)).then(|| (k.clone(), v.clone()))
                                }).collect())
                            ))
                        } else {
                            None
                        }
                    })
                })
                .collect();
            Ok(Byml::Hash(diff).to_text().as_bytes().to_vec())
        } else {
            Err(RustError::BymlError(roead::byml::BymlError::TypeError))
        }
    })?;
    Ok(PyBytes::new(py, &diff).into())
}

#[pyfunction]
fn merge_actorinfo(py: Python, modded_actors: Vec<u8>) -> PyResult<()> {
    Ok(py.allow_threads(|| -> Result<()> {
        let modded_actor_root = Byml::from_binary(&modded_actors).unwrap();
        let modded_actors: ActorMap = modded_actor_root.as_hash().unwrap().into_par_iter().map(|(h, a)| (h.parse::<u32>().unwrap(), a.clone())).collect();
        let mut merged_actors = stock_actorinfo()?.clone();
        merge_actormap(&mut merged_actors, &modded_actors);
        let (hashes, actors): (Vec<Byml>, Vec<Byml>) = merged_actors
            .into_iter()
            .map(|(hash, actor)| {
                (
                    if hash < 2147483648 {
                        Byml::Int(hash as i32)
                    } else {
                        Byml::UInt(hash)
                    },
                    actor,
                )
            })
            .unzip();
        let merged_actorinfo = Byml::Hash(
            [
                ("Actors".to_owned(), Byml::Array(actors)),
                ("Hashes".to_owned(), Byml::Array(hashes)),
            ]
            .into_iter()
            .collect(),
        );
        let output = util::settings()
            .master_mod_dir()
            .join("Actor/ActorInfo.product.sbyml");
        if !output.parent().unwrap().exists() {
            std::fs::create_dir_all(output.parent().unwrap())?;
        }
        std::fs::write(
            output,
            compress(merged_actorinfo.to_binary(util::settings().endian())),
        )?;
        Ok(())
    })?)
}
