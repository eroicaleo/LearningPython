#!/usr/local/bin/python3.3

L = [1, 2, 4, 8, 16, 32]
X = 5

# First edition
found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1

if found:
    print('at index', i)
else:
    print(X, 'not found')

# improvement a)
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i+1
else:
    print(X, 'not found')

# improvement b)
for d in L:
    if 2 ** X == d:
        print('at index', L.index(d))
        break
    else:
        i = i+1
else:
    print(X, 'not found')

# improvement c)
if 2 ** X in L:
    print('at index', L.index(d))
else:
    print(X, 'not found')

# improvement d)
L = [2 ** X for X in range(6)]
if 2 ** X in L:
    print('at index', L.index(d))
else:
    print(X, 'not found')


