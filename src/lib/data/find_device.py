from itertools import groupby
from typing import Any, Dict, List, Tuple
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from utils import get_all_addresses, group_by, load_json, dict_to_np, write_json
from LogScaler import LogScaler


def data_to_np(
    data: list[Dict[str, Any]], keys: List[str]
) -> Tuple[np.ndarray, list[list[Any]]]:
    location = [
        [entry["location"]["latitude"], entry["location"]["longitude"]]
        for entry in data
    ]
    signals = [
        {
            wifiInfo["address"]: wifiInfo["signalLevel"]
            for wifiInfo in entry["signature"]
        }
        for entry in data
    ]
    x = dict_to_np(signals, -100, keys)
    y = np.array(location)
    return x, y

data_set = load_json("./signals.json")
available_keys = get_all_addresses(data_set)
train_set = [entry for entry in data_set if not entry["deviceId"].startswith("7d8dc")]
test_set = [entry for entry in data_set if entry["deviceId"].startswith("7d8dc")]

# train_set = group_by(train_set, "deviceId")

x_train, y_train = data_to_np(train_set, available_keys)
x_test, y_test = data_to_np(test_set, available_keys)

x_scaler = make_pipeline(LogScaler())
x_train_scaled = x_scaler.fit_transform(x_train)
x_test_scaled = x_scaler.fit_transform(x_test)

y_scaler = make_pipeline(StandardScaler())
y_train_scaled = y_scaler.fit_transform(y_train)

knn = KNeighborsRegressor(n_neighbors=3, metric="euclidean", weights="distance")
knn.fit(x_train_scaled, y_train_scaled)

y_pred_scaled = knn.predict(x_test_scaled)  # (knn.predict(x_test_scaled) + y_test) / 2
y_pred = y_scaler.inverse_transform(y_pred_scaled)

# create signals.json to display predicted data
new_test_set = [
    {
        **entry,
        "deviceId": "prediction",
        "location": {"latitude": pred[0], "longitude": pred[1]},
    }
    for entry, pred in zip(test_set, y_pred)
]
write_json(
    test_set[-1:-2:-1] + new_test_set[-1:-2:-1] + train_set, "./pred_signals.json"
)
