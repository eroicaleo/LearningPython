#!/usr/bin/env python3

print([x*x for x in range(10)])

print((x*x for x in range(10)))
print(list(x*x for x in range(10)))

print({x*x for x in range(10)})
print({x: x*x for x in range(10)})

X = 99
print(X)
print([X for X in range(4)])
print(X)

Y = 99
for Y in range(5): pass

print(Y)

X = 'aaa'
def func():
    Y = 'bb'
    print(''.join(Z for Z in X + Y))

func()

print({x*x for x in range(10)})
print(set(x*x for x in range(10)))

print({x: x*x for x in range(10)})
print(dict((x, x*x) for x in range(10)))

print([x+y for x in [1, 2, 3] for y in [4, 5, 6]])
print({x+y for x in [1, 2, 3] for y in [4, 5, 6]})
print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})

print({x+y for x in 'ab' for y in 'cd'});
print({x+y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'})
print({x*2 for x in ['spam', 'ham', 'sausage'] if x[0] == 's'})
print({x.upper(): x*2 for x in ['spam', 'ham', 'sausage'] if x[0] == 's'})
