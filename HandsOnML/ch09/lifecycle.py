#!/usr/bin/env python

import tensorflow as tf

w = tf.constant(3)
x = w + 2
y = x + 5
z = x * 3
t = tf.Variable(0)
t_acc = tf.assign(t, t + 1)
s = t + 1

with tf.Session() as sess:
    print(y.eval())
    print(sess.run(y))
    print(z.eval())

with tf.Session() as sess:
    y_val, z_val = sess.run([y, z])
    print(y_val)
    print(z_val)

with tf.Session() as sess:
    t.initializer.run()
    print(sess.run(t_acc))
    print(sess.run(t_acc))
    print(sess.run(t_acc))
    print(sess.run(t_acc))
    print(sess.run(s))
    print('s ' = sess.run(s))

