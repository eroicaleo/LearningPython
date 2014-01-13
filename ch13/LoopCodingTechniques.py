#!/usr/local/bin/python3.3

print(list(range(5)))
print(list(range(2, 5)))
print(list(range(0, 10, 2)))
print(list(range(-5, 5, 1)))
print(list(range(5, -5, -1)))

for i in range(3):
    print(i, 'Pythons')

X = 'spam'
for x in X:
    print(x, end=' ')
print()

i = 0
while i < len(X):
    print(X[i], end=' ')
    i += 1
print()

for i in list(range(len(X))):
    print(X[i], end=' ')
print()

S = 'spam'
for i in list(range(len(X))):
    S = S[-1] + S[:-1]
    print(S, end=' ')
print()

S = 'spam'
for i in list(range(len(X))):
    S = S[1:] + S[0]
    print(S, end=' ')
print()

L = [1, 2, 3]
for i in list(range(len(L))):
    X = L[i:] + L[:i]
    print(X, end=' ')
print()

S = 'abcdefghijk'
for c in S[::2]:
    print(c, end=' ')
print()

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
print(zip(L1, L2))
print(list(zip(L1, L2)))

for (x, y) in zip(L1, L2):
    print(x, '+', y, '->', x+y)

S1 = 'abc'
S2 = '123xyz'
print(list(zip(S1, S2)))

S = 'spam'
print(list(map(ord, S)))

keys = ['spam', 'ham', 'eggs']
vals = [1, 3, 5]

D3 = dict(zip(keys, vals))
print(D3)

D4 = {k: v for (k, v) in zip(keys, vals)}
print(D4)

S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appreas at', offset)

E = enumerate(S)
print(E)
print(next(E))

print([c * i for (i, c) in enumerate(S)])

for (i, line) in enumerate(open('text.txt')):
    print('%s) %s' % (i, line.rstrip()))
    print('{0}) {1}'.format(i, line.rstrip()))

