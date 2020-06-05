#!/usr/bin/env python3

class Solution:
    def findRotateSteps(self, ring, key):
        di, l = {}, len(ring)
        for i, c in enumerate(ring):
            di.setdefault(c, []).append(i)
        print(di)

        def neighbor(i, c):
            d = di[c]
            print(f'in neighbor, c = {c}, d = {d}')
            if len(d) < 3 or i < d[0] or i > d[-1]:
                return [0, -1]
            else:
                lo, hi = 0, len(d)-1
                # find the first d[mi] <= i
                while lo < hi-1:
                    mi = lo+(hi-lo)//2
                    if d[mi] < i:
                        lo = mi
                    elif d[mi] > i:
                        hi = mi-1
                        if d[hi] < i:
                            return [hi,hi+1]
                return [lo,lo+1]

        prev, pc = [min(i, l-i) for i in di[key[0]]], key[0]
        print(f'prev = {prev}')
        for c in key[1:]:
            if c == pc:
                continue
            curr = []
            for i in di[c]:
                r, s = neighbor(i, pc)
                print(f'i = {i}, r = {r}, s = {s}')
                curr.append(min(prev[r]+abs(i-di[pc][r]), prev[r]+l-abs(i-di[pc][r]), prev[s]+abs(i-di[pc][s]), prev[s]+l-abs(i-di[pc][s])))
            prev, pc = curr, c
            print(f'prev = {prev}')
        return min(prev)+len(key)


ring = 'godding'
key = 'gd'
sol = Solution()
import random
import string
random.seed(46)
ring = ''.join(random.choices('abcdedfg', k=20))
key = ''.join(random.choices('abcdedfg', k=4))
print(f'ring = {ring}, key = {key}')
print(sol.findRotateSteps(ring, key))
