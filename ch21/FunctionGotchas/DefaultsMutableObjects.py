#!/usr/bin/env python3

print("default growing!")
def saver(x=[]):
    x.append(1)
    print(x)

saver([2])
saver()
saver()
saver()

print("default not growing!")
def saver(x=None):
    x = x or []
    x.append(1)
    print(x)

saver([2])
saver()
saver()
saver()

print("Function attributes")
def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []
saver()
saver()
saver()

