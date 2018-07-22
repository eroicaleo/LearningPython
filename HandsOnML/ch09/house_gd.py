#!/usr/bin/env python

import numpy as np
import tensorflow as tf
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

learning_rate = 0.01
n_epochs = 10000

def scaler_norm(a):
    return StandardScaler().fit(a).transform(a)

housing = fetch_california_housing()
m, n = housing.data.shape

housing_data_norm = scaler_norm(housing.data)
housing_data_plus_bias = np.c_[np.ones((m, 1)), housing_data_norm]
y_norm = scaler_norm(housing.target.reshape(-1, 1))

X = tf.constant(housing_data_plus_bias, dtype=tf.float32, name='X')
y = tf.constant(y_norm, dtype=tf.float32, name='y') 
XT = tf.transpose(X)
theta = tf.Variable(tf.random_uniform([n+1, 1], -1.0, 1.0), dtype=tf.float32, name='theta')
y_pred = tf.matmul(X, theta)
error = y_pred - y
mse = tf.reduce_mean(tf.square(error), name='mse')
gradients = 2 / m * tf.matmul(XT, error)
training_op = tf.assign(theta, theta - learning_rate * gradients)

init = tf.global_variables_initializer()

print('#'*80)
print('## Gradient descent')
print('#'*80)
with tf.Session() as sess:
    init.run()

    for epoch in range(n_epochs):
        if epoch % 100 == 0:
            print('Epoch', epoch, 'MSE = ', mse.eval())
        sess.run(training_op)

    best_theta = theta.eval()
    print(best_theta)

print('#'*80)
print('## Verifying with equation')
print('#'*80)
theta_cal = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)
y_pred_cal = tf.matmul(X, theta_cal)
error_cal = y_pred_cal - y
mse_cal = tf.reduce_mean(tf.square(error_cal), name='mse')

with tf.Session() as sess:
    init.run()
    theta_cal_val, mse_cal = sess.run([theta_cal, mse_cal])
    print(theta_cal_val, mse_cal)
