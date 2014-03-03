#!/usr/local/bin/python3.3

def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

L = [1, 2, 3, 4, 5]
print(mysum(L))

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)

print(mysum(L))

print(mysum(['spam', 'ham', 'eggs']))

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))

print(L)
def sumtree1(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            print(front, end=', ')
            tot += front
        else:
            items.extend(front)
    return tot
print(sumtree1(L))

def sumtree2(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            print(front, end=', ')
            tot += front
        else:
            items[:0] = front
    return tot
print(sumtree2(L))
