#!/usr/local/bin/python3.3

x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]
print();

a = 0; b = 10
while a < b:
    print(a, end=' ')
    a += 1
print();

a = 0; b = 10
while True:
    print(a, end=' ')
    a += 1
    if a >= b: break
print();

x = 10
while x > 0:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=' ')
print();

# while True:
#     name = input('Enter name:')
#     if name == 'stop': break
#     age = input('Enter age:')
#     print('Hello', name, '=>', int(age) ** 2)

y = 23
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is a prime')

y = 10
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is a prime')

