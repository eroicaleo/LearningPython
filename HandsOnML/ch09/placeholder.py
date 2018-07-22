#!/usr/bin/env python

import numpy as np
import tensorflow as tf

A = tf.placeholder(tf.float32, shape=(None, 3))
B = A + 5

with tf.Session() as sess:
    res = sess.run(B, feed_dict = {A : [[1, 2, 3]]})
    print(res)
    res = sess.run(B, feed_dict = {A : [[1, 2, 3], [4, 5, 6]]})
    print(res)
