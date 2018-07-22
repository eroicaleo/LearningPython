#!/usr/bin/env python

import tensorflow as tf

x1 = tf.Variable(1)
print(x1.graph is tf.get_default_graph())

graph = tf.Graph()
with graph.as_default():
    x2 = tf.Variable(2)

print(x2.graph is graph)
print(x2.graph is tf.get_default_graph())

graph0 = tf.get_default_graph()
print(x1.graph is graph0)
