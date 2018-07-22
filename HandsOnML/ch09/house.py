#!/usr/bin/env python

import numpy as np
import tensorflow as tf
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
m, n = housing.data.shape
print(housing.data.shape)
print(housing.target.shape)

housing_data_plus_bias = np.c_[np.ones((m, 1)), housing.data]
print(housing_data_plus_bias.shape)
print(housing_data_plus_bias[0])

y = housing.target.reshape(-1, 1)
print(y.shape)

X = tf.constant(housing_data_plus_bias, dtype=tf.float32, name='X')
y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name='y') 
XT = tf.transpose(X)
theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)

with tf.Session() as sess:
    theta_val = theta.eval()

print(theta_val)
