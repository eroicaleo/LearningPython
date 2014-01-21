#!/usr/local/bin/python3.3

X = 88

print(X)

def func():
    global X
    X = 99
    return

func()
print(X)

y, z = 1, 2
def func2():
    global x
    x = y + z
    return x

print(func2())
y, z = 3, 4
print(func2())
