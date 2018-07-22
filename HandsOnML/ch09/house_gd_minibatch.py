#!/usr/bin/env python

import numpy as np
import tensorflow as tf
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

learning_rate = 0.01
n_epochs = 1000
batch_size = 100

def scaler_norm(a):
    return StandardScaler().fit(a).transform(a)

def fetch_batch(epoch, batch_index, batch_size):
    batch_start = batch_index * batch_size
    batch_end   = batch_start + batch_size - 1
    if  batch_end > m:
        batch_end = m - 1
    return housing_data_plus_bias[batch_start:batch_end], y_norm[batch_start:batch_end]

housing = fetch_california_housing()
m, n = housing.data.shape
n_batches = int(np.ceil(m / batch_size))

housing_data_norm = scaler_norm(housing.data)
housing_data_plus_bias = np.c_[np.ones((m, 1)), housing_data_norm]
y_norm = scaler_norm(housing.target.reshape(-1, 1))

X = tf.placeholder(dtype=tf.float32, shape=(None, n+1), name='X')
y = tf.placeholder(dtype=tf.float32, shape=(None, 1), name='y') 
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
        for batch_index in range(n_batches):
            # print(epoch, batch_index)
            X_batch, y_batch = fetch_batch(epoch, batch_index, batch_size)
            sess.run(training_op, feed_dict={X: X_batch, y: y_batch})
        if epoch % 100 == 0:
            print('Epoch', epoch, 'MSE = ', mse.eval(feed_dict={X: housing_data_plus_bias, y: y_norm}))

    best_theta = theta.eval()
    print(best_theta)

# print('#'*80)
# print('## Verifying with equation')
# print('#'*80)
# theta_cal = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)
# y_pred_cal = tf.matmul(X, theta_cal)
# error_cal = y_pred_cal - y
# mse_cal = tf.reduce_mean(tf.square(error_cal), name='mse')
# 
# with tf.Session() as sess:
#     init.run()
#     theta_cal_val, mse_cal = sess.run([theta_cal, mse_cal])
#     print(theta_cal_val, mse_cal)

