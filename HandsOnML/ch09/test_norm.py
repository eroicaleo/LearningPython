#!/usr/bin/env python

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing

def scaler_norm(a):
    return StandardScaler().fit(a).transform(a)

housing = fetch_california_housing()
m, n = housing.data.shape
print(m, n)
housing_data_norm = scaler_norm(housing.data)
housing_data_plus_bias = np.c_[np.ones((m, 1)), housing_data_norm]
y_norm = scaler_norm(housing.target.reshape(-1, 1))

print(np.mean(y_norm, axis=0))
# print(np.mean(housing_data_norm, axis=0))
# print(housing_data_plus_bias[0:2])

a = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
print(a)
print(a.shape)
a_norm = scaler_norm(a)
print(a_norm)

def fetch_batch(epoch, batch_index, batch_size):
    batch_start = batch_index * batch_size
    batch_end   = batch_start + batch_size - 1
    if  batch_end > m:
        batch_end = m - 1
    return housing_data_plus_bias[batch_start:batch_end], y_norm[batch_start:batch_end]

n_batches = int(np.ceil(m / 100))
print(n_batches)
# print(fetch_batch(0, 207, 100))

# scaler.fit(housing_data_plus_bias)
# housing_data_plus_bias_norm = scaler.transform(housing_data_plus_bias)
# print(scaler.mean_)
# print(housing_data_plus_bias_norm[0:2])
