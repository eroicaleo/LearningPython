#!/usr/bin/env python3

print('I am', __name__)

def minmax2(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(res, arg):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

if __name__ == '__main__':
    print(minmax2(lessthan, 4, 2, 1, 5, 6, 3))
    print(minmax2(grtrthan, 4, 2, 1, 5, 6, 3))
