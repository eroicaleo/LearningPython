#!/usr/bin/env python

import numpy as np
import tensorflow as tf
from datetime import datetime

now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
root_logdir = 'tf_logs'
log_dir = '{}/run-{}/'.format(root_logdir, now)

def relu(X):
    with tf.variable_scope('relu', reuse=True):
        threshold = tf.get_variable("threshold")
        wshape = (int(X.get_shape()[1]), 1)
        w = tf.Variable(tf.random_normal(wshape), name='weights')
        b = tf.Variable(0.0, name='bias')
        z = tf.add(tf.matmul(X, w), b, name="z")
        relu = tf.maximum(z, threshold, name="relu")
        return relu

with tf.variable_scope('relu'):
    threshold = tf.get_variable("threshold", shape=(), initializer=tf.constant_initializer(0.0))
n_features = 3
X = tf.placeholder(tf.float32, shape=(None, n_features), name='X')
relus = [relu(X) for i in range(5)]
output = tf.add_n(relus, name='relus')
assign_op = threshold.assign(5)

init = tf.global_variables_initializer()

file_writer = tf.summary.FileWriter(log_dir, tf.get_default_graph())

with tf.Session() as sess:
    init.run()

    assign_op.eval()
    res = output.eval(feed_dict={X: np.array([1, 2, 3]).reshape(1, 3)})
    print(res)

file_writer.close()
