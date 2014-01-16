#!/usr/local/bin/python3.3

M = map(lambda x: x ** 2, range(3))

for i in M: print(i)
for i in M: print(i)

print(list(range(10)))

M = map(abs, [-1, 1, 0])
for i in M: print(i)
for i in M: print(i)

Z = zip((1, 2, 3), (4, 5, 6))
print(list(Z))
print("the zip object has been exhausted")
print(list(Z))

Z = zip((1, 2, 3), (4, 5, 6))
print(next(Z))
print(next(Z))

print(filter(bool, ['spam', '', 'ni']))
print(list(filter(bool, ['spam', '', 'ni'])))

D = {'a': 1, 'b': 2, 'c': 3}
for k in sorted(D) : print(k, D[k], end=' ')
print()
