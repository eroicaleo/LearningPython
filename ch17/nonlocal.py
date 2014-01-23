#!/usr/local/bin/python3.3

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(state, label)
        state += 1
    return nested

F = tester(0)
F('spam')
F('ham')
F('eggs')

G = tester(42)
G('spam')
G('ham')
G('eggs')


class tester:
    def __init__(self, start):
        self.state = start
    def nested(self, label):
        print(label, self.state)
        self.state += 1

F = tester(0)
F.nested('spam')
F.nested('ham')
F.nested('eggs')

print(F.state)
print(F.state)

G = tester(42)
G.nested('spam')
G.nested('ham')
G.nested('eggs')

class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):
        print(label, self.state)
        self.state += 1

H = tester(99)
H('spam')
H('ham')
H('eggs')

def tester(start):
    def nested(label):
        print(nested.state, label)
        nested.state += 1
    nested.state = start
    return nested

F = tester(0)
F('spam')
F('ham')
F('eggs')
print(F.state)

G = tester(42)
G('spam')
G('ham')
G('eggs')
print(G.state)
print(F is G)


