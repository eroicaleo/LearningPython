#!/usr/local/bin/python3.3

# 1
L = [0] * 5
print(L)

L = [0, 0, 0, 0, 0]
print(L)

L = [0 for i in range(0, 5)]
print(L)

# 2
D = {}
D = D.fromkeys(['a', 'b'], 0)
print(D)
D = {}
D = dict(zip(['a', 'b'], [0, 0]))
print(D)
