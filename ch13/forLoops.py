#!/usr/local/bin/python3.3

for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')
print()

sum = 0
for x in [1, 2, 3, 4]:
    sum += x
print(sum)

prod = 1
for x in [1, 2, 3, 4]:
    prod *= x
print(prod)

S = 'lumberjack'
for x in S:
    print(x, end=' ')
print()

T = ['and', "I'm", 'OK']
for x in T:
    print(x, end=' ')
print()

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])

print(D.items())
print(list(D.items()))

for (key, value) in D.items():
    print(key, '=>', value)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)

for ((a, b), c) in [((1, 2), 3), ('XY', 6)]:
    print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

items = ['aaa', 111, (4, 5), 2.01]
keys = [(4, 5), 3.14]

for key in keys:
    for item in items:
        if key == item:
            print(key, 'was found!')
            break
    else:
        print(key, 'not found!')

print('Use in operator')
for key in keys:
    if key in items:
        print(key, 'was found!')
    else:
        print(key, 'not found!')


for line in open('text.txt').readlines():
    print(line.rstrip())

for line in open('text.txt'):
    print(line.rstrip())
