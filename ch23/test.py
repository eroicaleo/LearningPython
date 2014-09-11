#!/usr/bin/env python3

import module1

module1.printer('')

from module1 import printer
printer('Hello world!')

from module1 import *
printer('Hello world!')

print('module1.spam =', module1.spam)
module1.spam = 2

import module1
print('module1.spam =', module1.spam)

from small import x, y
print("x: ", x)
print("y: ", y)

x = 42
y[0] = 42

import small
print("x: ", small.x)
print("y: ", small.y)

