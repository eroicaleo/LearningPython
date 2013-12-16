#!/usr/local/bin/python3.3

T = (1, 2)
print(T)

T = T + (3, 4)
print(T)

T = (1, 2) * 4
print(T)

x = (40)
print(x)

y = (40,)
print(y)

T = ('cc', 'aa', 'bb', 'dd')
print(T)
L = list(T)
print(L)
L.sort()
print(L)
T = tuple(L)
print(T)
T = ('cc', 'aa', 'bb', 'dd')
print(T)
print(sorted(T))

T = (1, 2, 3, 4, 5)
print(T)
L = [x+20 for x in T]
print(L)
T = tuple(L)
print(T)

T = (1, 2, 3, 2, 4, 2)
print(T.index(2))
print(T.index(2, 2))
print(T.count(2))

T = (1, [2, 3], 4)
print(T)
T[1][0] = 'spam'
print(T)

bob = ('Bob', 40.5, ['dev', 'mgr'])
print(bob)

bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob)

print(tuple(bob.values()))

from collections import namedtuple

Rec = namedtuple('Rec', ['name', 'age', 'job'])
bob = Rec('Bob', age=40.5, job=['dev', 'mgr'])
print(bob)

print((bob[0], bob[2]))
print((bob.name, bob.job))

O = bob._asdict()
print(O)
print((O['name'], O['job']))

name, age, job = bob
print((name, age))
for x in bob:
    print(x)
