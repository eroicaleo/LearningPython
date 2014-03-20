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

for x in (x**2 for x in range(4)):
    print('%s, %s' % (x, x / 2.0))

s = ''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))
print(s)

a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(a, c)

print(sum(x**2 for x in range(4)))
print(sorted(x**2 for x in range(4)))
print(sorted((x**2 for x in range(4)), reverse=True))
