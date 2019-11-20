#!/usr/bin/env python

def print_banner(s):
    print('##------------------------------------------------------------------------------')
    print(f'## {s}')
    print('##------------------------------------------------------------------------------')

print_banner('Shallow copies')

xs = [[1,2,3], [4,5,6], [7,8,9]]
ys = list(xs)
print(xs)
print(ys)
xs.append(['new sublist'])
print(xs)
print(ys)
xs[1][0] = 'X'
print(xs)
print(ys)

print_banner('deep copies with copy.deepcopy')
import copy
xs = [[1,2,3], [4,5,6], [7,8,9]]
zs = copy.deepcopy(xs)
print(xs)
print(zs)
xs[1][0] = 'X'
print(xs)
print(zs)

print_banner('copy with arbitrary object')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

a = Point(23, 42)
print(a)
b = copy.copy(a)
print(b)
print('a is b?', a is b)

print_banner('copy Rectangle object')

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')

rect = Rectangle(Point(0, 1), Point(5, 6))
print(rect)
srect = copy.copy(rect)
print(srect)
print('rect is srect? ', rect is srect)
rect.topleft.x = 999
print(rect)
print(srect)
drect = copy.deepcopy(rect)
rect.topleft.x = 222
print(rect)
print(drect)
