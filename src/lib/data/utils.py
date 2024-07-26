import json
from itertools import groupby
from typing import Any, Dict, List
import numpy as np


def load_json(file_name: str) -> List[Dict[str, Any]]:
    with open(file_name) as fp:
        return json.load(fp)


def dict_to_np(data: List[Dict[str, Any]], default: Any, keys: List[str]) -> np.ndarray:
    return np.array([[entry.get(key, default) for key in keys] for entry in data])


def get_all_addresses(data: List[Dict[str, Any]]) -> List[str]:
    return list(
        set(signal["address"] for entry in data for signal in entry["signature"])
    )

def write_json(data: List[Dict[str, Any]],file_name: str):
    with open(file_name,"w") as fp:
        json.dump(data,fp)

def group_by(data: list[Dict[str, Any]], key: str) -> list[Dict[str, Any]]:
    get_key_lambda = lambda it: it[key]
    return [
        average_ss(list(group), value)
        for value, group in groupby(sorted(data, key=get_key_lambda), get_key_lambda)
    ]

def average_ss(data: list[Dict[str, Any]], key) -> Dict[str, Any]:
    new_dict = {**data[0]}
    default = float("-inf")
    new_ss = {
        ap["address"]: {**ap, "signalLevel": default}
        for ap in new_dict["signature"]
    }
    for info in data:
        for ap in info["signature"]:
            if ap["address"] not in new_ss:
                new_ss.setdefault(ap["address"], {**ap, "signalLevel": default})
            new_ss[ap["address"]]["signalLevel"] = max(
                new_ss[ap["address"]]["signalLevel"], ap["signalLevel"]
            )
            # new_ss[ap["address"]]["signalLevel"] += ap["signalLevel"]
    # for key in new_ss.keys():
    #     new_ss[key]["signalLevel"] /= len(data)
    new_dict["signature"] = list(new_ss.values())
    return new_dict
