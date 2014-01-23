#!/usr/local/bin/python3.3

X = 99
def f1():
    X = 88
    def f2():
        print(X)
    return f2

action = f1()
action()

def maker(N):
    def action(X):
        return X ** N;
    return action

f = maker(2)
print(f)
print(f(3))
print(f(4))

g = maker(3)
print(g(4))
print(f(4))

def maker(N):
    return lambda X: X ** N

h = maker(4)
print(h(4))

def f1():
    x = 88
    def f2(x=x):
        print(x)
    f2()

f1()

def func():
    x = 4
    action = lambda n: x ** n
    return action

x = func()
print(x(4))

def func():
    x = 4
    action = lambda n, x=x: x ** n
    return action

x = func()
print(x(4, 5))

def makeActions():
    res = []
    for i in range(5):
        res.append(lambda x: i ** x)
    return res

acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print(acts[4](2))

def makeActions():
    res = []
    for i in range(5):
        res.append(lambda x, i=i: i ** x)
    return res

acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print(acts[4](2))
