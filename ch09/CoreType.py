#!/usr/local/bin/python3.3

X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y': 2}

X[1] = 'surprise'
print(X)
print(L)
print(D)

L = [1, 2, 3]
D = {'a': 1, 'b': 2}
A = L[:]
B = D.copy()
A[1] = 'Ni!'
B['c'] = 'spam'
print(A)
print(B)
print(L)
print(D)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]

print(L1 == L2)
print(L1 is L2)

s1 = 'spam'
s2 = 'spam'
print(s1 == s2, s1 is s2)

s1 = 'a very very very very very longer string'
s2 = 'a very very very very very longer string'
print(s1 == s2, s1 is s2)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]

print(L1 == L2, L1 < L2, L1 > L2)
