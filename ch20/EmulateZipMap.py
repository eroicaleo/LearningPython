#!/usr/bin/python3.3

S1 = 'abc'
S2 = 'xyz123'
z = zip(S1, S2)
print(list(z))

print(list(zip([1, 2, 3], [2, 3, 4, 5])))

print(list(map(abs, [-2, -1, 0, 1, 2])))

print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))

print(list(map(lambda x, y: x+y, open('script2.py'), open('script2.py'))))

print([x+y for (x, y) in zip(open('script2.py'), open('script2.py'))])
