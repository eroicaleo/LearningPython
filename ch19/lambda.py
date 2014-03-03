#!/usr/local/bin/python3.3

f = lambda a, b, c: a+b+c
print(f(2, 3, 4))

x = lambda a='fee', b='fie', c='foe': a+b+c
print(x('wee'))

def knights():
    title = 'Sir'
    action = lambda x: title + ' ' + x
    return action

act = knights()
msg = act('Robin')
print(msg)

L = [lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4,
    ]

for f in L:
    print(f(2))

print(L[0](3))

# multiple branch switch

D = {
        'already': lambda: 2 + x,
        'got'    : lambda: 2 * 4,
        'one'    : lambda: 2 ** 6
        }

print(D['one']())

lower = (lambda x, y: x if x < y else y)
print(lower('aa', 'bb'))
print(lower('bb', 'aa'))

import sys
showall = lambda x: list(map(sys.stdout.write, x))
print(showall(["spam\n", "eggs\n", "ham\n"]))
showall = lambda x: map(sys.stdout.write, x)
print(list(showall(["spam\n", "eggs\n", "ham\n"])))

showall = lambda x: [print(line, end='') for line in x]
showall(["spam\n", "eggs\n", "ham\n"])
showall = lambda x: print(*x, end='', sep='')
showall(["spam\n", "eggs\n", "ham\n"])

def action(x):
    return lambda y: x+y

act = action(99)
print(act(2))

action = lambda x: lambda y: x+y
act = action(101)
print(act(3))


