#!/usr/local/bin/python3.3

a, *b = 'spam'
print(a)
print(b)

nudge = 1
wink = 2
print(nudge, wink)
A, B = nudge, wink
print([A, B])
[C, D] = [nudge, wink]
nudge, wink = wink, nudge
print(nudge, wink)

[a, b, c] = (1, 2, 3)
print(a, c)
(a, b, c, d) = "SPAM"
print(a, c)

D = {'a': 'lala', 'b': 'haha'}
[g, y] = D
print([g, y])

string = 'SPAM'
a, b, c = string[0], string[1], string[2:]
print(a, b, c)

a, b, c = list(string[:2]) + [string[2:]]
print(a, b, c)

(a, b), c = string[:2], string[2:]
print(a, b, c)

red, blue, green = range(3)
print(red, blue)

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
a, *b = seq
print(a)
print(b)

*a, b = seq
print(a)
print(b)

a, *b, c = seq
print(a)
print(b)
print(c)

L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)

a, b, c, *d = seq
print(a, b, c, d)
a, b, c, d, *e = seq
print(a, b, c, d, e)

# These are errors

# a, *b, c, *d = seq
*a, = seq
print(a)

a, *b = seq
print(a, b)
a, b = seq[0], seq[1:]
print(a, b)

*a, b = seq
print(a, b)
a, b = seq[:-1], seq[-1]
print(a, b)

a = b = c = 'spam'
print(a, b, c)

a = b = []
print(a, b)
b.append(42)
print(a, b)

a, b = [], []
print(a, b)
b.append(42)
print(a, b)

L = [1, 2]
M = L
L = L + [3, 4]
print(L, M)
L = [1, 2]
M = L
L += [3, 4]
print(L, M)
