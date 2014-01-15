#!/usr/local/bin/python3.3

for x in [1, 2, 3, 4]: print(x ** 2, end=' ')
print()


for x in [1, 2, 3, 4]: print(x ** 3, end=' ')
print()

for x in 'spam': print(x * 2, end=' ')
print()

print('The Iteration Protocol: File Iterators')
print(open('script2.py').read())
f = open('script2.py')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
f.close()

f = open('script2.py')
print(f.__next__(), end='')
print(f.__next__(), end='')
print(f.__next__(), end='')
print(f.__next__(), end='')
print(f.__next__(), end='')
print(
"""one more
print(f.__next__())
causes StopIteration exception."""
)
# print(f.__next__())
f.close()

f = open('script2.py')
for line in f:
    print(line.upper(), end='')
f.close()

print('# Using while loop')
f = open('script2.py')
while True:
    line = f.readline()
    if not line: break
    print(line.upper(), end='')
f.close()

# Manual Iteration

L = [1, 2, 3]
I = iter(L)
print(I.__next__())
print(I.__next__())
print(I.__next__())
# print(I.__next__())
print(
"""one more
print(I.__next__())
causes StopIteration exception."""
)

print('file itself is an iterator object')
f = open('script2.py')
print(f == iter(f))
print(f == f.__iter__())
f.close()

L = [1, 2, 3]
for x in L: print(x ** 2, end=' ')
print()

# manual iteration
I = iter(L)
while True:
    try:
        print(next(I) ** 2, end=' ')
    except StopIteration:
        break
print()

D = {1: 'a', 2: 'b', 3: 'c'}
I = iter(D)
print(next(I))
print(next(I))
print(next(I))

import os
P = os.popen('ls')
print(P.__next__(), end='')
print(P.__next__(), end='')

P = os.popen('ls')
I = iter(P)
print(next(I), end='')
print(next(I), end='')

R = range(5)
print(R)
I = iter(R)
print(next(I))
print(next(I))

E = enumerate('spam')
I = iter(E)
print(next(I))
print(next(I))
print(list(E))
