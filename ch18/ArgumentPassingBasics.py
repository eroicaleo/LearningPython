#!/usr/local/bin/python3.3

def f(a):
    a = 99
    return

b = 88
f(b)
print(b)

def changer(a, b):
    a = 2
    b[0] = 'spam'

X = 0
L = [1, 2]

changer(X, L)
print(X, L)

X = 0
L = [1, 2]
def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y

X, L = multiple(X, L)
print(X, L)


