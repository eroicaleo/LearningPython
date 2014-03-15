#!/usr/local/bin/python3.3

res = map(ord, 'spam')
print(list(res))

res = [ord(x) for x in 'spam']
print(res)

print([x ** 2 for x in range(10)])
print(list(map(lambda x: x ** 2, range(10))))

print([x for x in range(5) if x % 2 == 0])
print(list(filter(lambda x: x % 2 == 0, range(5))))

print([x ** 2 for x in range(10) if x % 2 == 0])
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10)))))

print([x+y for x in [0, 1, 2] for y in [100, 200, 300]])

print([x+y for x in 'spam' for y in 'SPAM'])

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])

M = [[y+x for y in range(3)] for x in [1, 4, 7]]
print(M)

N = [[x] * 3 for x in [1, 2, 3]]
print(N)
