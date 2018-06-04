#!/usr/bin/env python

class adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self, other):
        self.data += other

x = adder()
print(x)
print(str(x))

class addrepr(adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data

x = addrepr(2)
x + 1
print(x)
print(str(x))

class addstr(adder):
    def __str__(self):
        return '[Value: %s]' % self.data

x = addstr(3)
x + 1
print(x)
print(repr(x))

class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data
    def __repr__(self):
        return 'addboth(%s)' % self.data

x = addboth(4)
x + 1
print(x)
print(repr(x))

class Printer():
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)

objs = [Printer(2), Printer(3)]
for x in objs: print(x)
print(objs)

class Printer():
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return str(self.val)

objs = [Printer(2), Printer(3)]
for x in objs: print(x)
print(objs)
