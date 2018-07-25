#!/usr/bin/env python

import numpy as np
import tensorflow as tf
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from datetime import datetime

now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
root_logdir = 'tf_logs'
log_dir = '{}/run-{}/'.format(root_logdir, now)

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

with tf.name_scope('loss') as scope:
    error = y_pred - y
    mse = tf.reduce_mean(tf.square(error), name='mse')

print(error.op.name)
print(mse.op.name)

gradients = 2 / m * tf.matmul(XT, error)
training_op = tf.assign(theta, theta - learning_rate * gradients)

init = tf.global_variables_initializer()

mse_summary = tf.summary.scalar('MSE', mse)
file_writer = tf.summary.FileWriter(log_dir, tf.get_default_graph())

with tf.Session() as sess:
    init.run()

file_writer.close()
