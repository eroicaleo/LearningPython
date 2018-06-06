#!/usr/bin/env python

class Spam:
    def doit(self, message):
        print(message)

object1 = Spam()
object1.doit('hello world!')
x = object1.doit
x('hello world!')
t = Spam.doit
t(object1, 'howdy!')

class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1
        x(42)

Eggs().m2()

class Selfless:
    def __init__(self, data):
        self.data = data
    def selfless(args1, args2):
        return args1 + args2
    def normal(self, args1, args2):
        return self.data + args1 + args2

X = Selfless(2)
print(X.normal(3, 4))
print(Selfless.normal(X, 3, 4))
print(Selfless.selfless(3, 4))

# The following twos have errors
# X.selfless(3, 4)
# Selfless.normal(3, 4)

class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3


x = Number(2)
y = Number(3)
z = Number(4)
print(x.double())
acts = [x.double, y.double, y.triple, z.double]
for act in acts:
    print(act())

bound = x.double
print(bound.__self__, bound.__func__)
print(bound.__self__.base)

def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val = val
    def __call__(self, arg):
        return self.val + arg

class Product:
    def __init__(self, val):
        self.val = val
    def method(self, arg):
        return self.val * arg

sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]

for act in actions:
    print(act(5))
print(actions[-1](5))
print([act(5) for act in actions])
print(list(map(lambda act: act(5), actions)))

class Negate:
    def __init__(self, val):
        self.val = -val
    def __repr__(self):
        return str(self.val)

actions = [square, sobject, pobject.method, Negate]
print([act(5) for act in actions])
table = {act(5) : act for act in actions}
for (key, value) in table.items():
    print('%2s => %s' % (key, value))
    # print('{0:2} => {1}'.format(key, value))
