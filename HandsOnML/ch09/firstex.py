#!/usr/bin/env python

import tensorflow as tf

x = tf.Variable(3, name='x')
y = tf.Variable(4, name='y')
f = x*x*y + y + 2

sess = tf.Session()
sess.run(x.initializer)
sess.run(y.initializer)
result = sess.run(f)
print(result)
sess.close()

with tf.Session() as sess:
    x.initializer.run()
    y.initializer.run()
    result = f.eval()
    print('This is from with session')
    print(result)

with tf.Session() as sess:
    tf.get_default_session().run(x.initializer)
    tf.get_default_session().run(y.initializer)
    result = f.eval()
    print('This is from with session and with get_default_session')
    print(result)


init = tf.global_variables_initializer()
with tf.Session() as sess:
    init.run()
    result = f.eval()
    print('This is from with session and with global_variables_initializer')
    print(result)

