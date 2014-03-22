#!/usr/bin/python3.3

def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i, end=":")
print()

x = gensquares(4)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# throw exception: StopIteration
# print(next(x))

def ups(line):
    for x in line.split(','):
        yield x.upper()

print(tuple(ups('aaa,bbb,ccc')))
print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})

G = (x**2 for x in range(4))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
# throw exception: StopIteration
# print(next(G))

# Generator expression
for x in (x**2 for x in range(4)):
    print('%s, %s' % (x, x / 2.0))

s = ''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))
print(s)

a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(a, c)

print(sum(x**2 for x in range(4)))
print(sorted(x**2 for x in range(4)))
print(sorted((x**2 for x in range(4)), reverse=True))

print(list(map(abs, [-1, -2, 3, 4])))
print(list(abs(x) for x in [-1, -2, 3, 4]))

print(list(map(lambda x: x * 2, (1, 2, 3, 4))))
print(list(x * 2 for x in (1, 2, 3, 4)))

# Compare between generator expression, list comprehension and map

line = "aaa,bbb,ccc"
print(''.join([x.upper() for x in line.split(',')]))
print(''.join(x.upper() for x in line.split(',')))
print(''.join(map(str.upper, line.split(','))))

print(''.join(x*2 for x in line.split(',')))
print(''.join(map(lambda x: x * 2, line.split(','))))

# filter v.s. generator expression
line = "aa bbb c"
print(''.join(x for x in line.split(' ') if len(x) > 1))
print(''.join(filter(lambda x: len(x) > 1, line.split(' '))))


print(''.join(x.upper() for x in line.split(' ') if len(x) > 1))
print(''.join(map(lambda x: x.upper(), filter(lambda x: len(x) > 1, line.split(' ')))))

res = ''
for x in line.split():
    if len(x) > 1:
        res += x.upper()
print(res)

# Generator functions Versus Generator expressions
G = (c * 4 for c in 'SPAM')
print(list(G))

def fourtimes(s):
    for c in s:
        yield c * 4

G = fourtimes('spam')
print(list(G))

G = (c * 4 for c in 'SPAM')
I = iter(G)
print(next(I))
print(next(I))

G = fourtimes('spam')
I = iter(G)
print(next(I))
print(next(I))

print(iter(G) is G)

G = (c * 4 for c in 'SPAM')
I = iter(G)
print(next(I))
print(next(I))

I2 = iter(G)
print(next(I2))

def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

print(list(both(5)))
print(" : ".join(str(i) for i in both(5)))
