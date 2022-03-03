#!/usr/bin/env python3

def cover(x, k):
    x = sorted(x)
    i = j = n = 0
    l = len(x)
    while True:
        while j < l and x[j]-k <= x[i]:
            j += 1
        j -= 1
        n += 1
        while i < l and x[j]+k >= x[i]:
            i += 1
        if i >= l:
            return n
        j = i

x = [7,2,4,6,5,9,12,11]
k = 2
x = [1,2,3,4,5]
k = 1
x = [1,2,3,5,9]
k = 1
print(cover(x, k))
