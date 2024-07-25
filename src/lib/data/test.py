# TODO
# Clean up code.
# create feature raws based on dictionary<address,SS>
# separate out my personal device data for testing the model - deviceId - 7d8dcfb.
# Try following preprocessing
# 1. average SS per AP for a single deviceId (only Pi devices)
# 2. minimum SS per AP for a single deviceId (only Pi devices)
# 3. convert dBm to mW
# Target mean absolute error < 1.0e-6
# Chart the spots generated in UI (generate another .json)

import numpy as np
import json
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

with open("signals.json") as fp:
    data = json.load(fp)

# transform data
location_data = []
signal_data = []

a = ""
a.startswith

for device_info in data:
    location_data.append(
        [device_info["location"]["latitude"], device_info["location"]["longitude"]]
    )
    signals = []
    for signal in sorted(device_info["signature"], key=lambda it: it["address"]):
        signals.append(signal["signalLevel"])
    signal_data.append(signals)

max_length = min([len(it) for it in signal_data])
signal_data = [it[:max_length] for it in signal_data]

x = np.array(signal_data)
y = np.array(location_data)

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(x)

# Normalize the target (latitude and longitude)
y_scaler = StandardScaler()
y_scaled = y_scaler.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, test_size=0.2, random_state=42
)

# Train k-NN model
knn = KNeighborsRegressor(n_neighbors=3, metric="euclidean")
knn.fit(X_train, y_train)

# Predict on test set
y_pred_scaled = knn.predict(X_test)
y_pred = y_scaler.inverse_transform(y_pred_scaled)

# Evaluate model
y_test_original = y_scaler.inverse_transform(y_test)
print(y_test_original)
print(y_pred)
mse = mean_absolute_error(y_test_original, y_pred)
print(f"Mean Squared Error: {mse}")
