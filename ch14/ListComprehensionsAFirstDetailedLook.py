#!/usr/local/bin/python3.3

L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print(L)

L = [1, 2, 3, 4, 5]
L = [x+10 for x in L]
print(L)

f = open('script2.py')
lines = f.readlines()
print(lines)
f.close()

lines = [line.rstrip() for line in open('script2.py')]
print(lines)

lines = [line.rstrip().upper() for line in open('script2.py')]
print(lines)

lines = [line.split() for line in open('script2.py')]
print(lines)

lines = [line.replace(' ', '!') for line in open('script2.py')]
print(lines)

lines = [('sys' in line, line[:5]) for line in open('script2.py')]
print(lines)

lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
print(lines)

lines = [line.rstrip() for line in open('script2.py') if line.rstrip()[-1].isdigit()]
print(lines)

lines = [x+y for x in 'abc' for y in 'lmn']
print(lines)

lines = [line.upper() for line in open('script2.py')]
print(lines)

print(list(map(str.upper, open('script2.py'))))

print(sorted(open('script2.py')))
print(list(zip(open('script2.py'), open('script2.py'))))

print(list(enumerate(open('script2.py'))))

a, b, c, d, e = open('script2.py')
print(a, b, c, d, e)

a, *b = open('script2.py')
print(a, b)

L = [11, 22, 33, 44]
L[1:3] = open('script2.py')
print(L)

L = [11]
L.extend(open('script2.py'))
print(L)

D = {ix: line for (ix, line) in enumerate(open('script2.py'))}
print(D)

A = (1, 2)
B = (3, 4)
print(list(zip(A, B)))
A, B = zip(*zip(A, B))
print(A, B)
