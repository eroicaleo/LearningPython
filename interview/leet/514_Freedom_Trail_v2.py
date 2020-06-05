#!/usr/bin/env python3

class Solution:
    def findRotateSteps(self, ring, key):
        di, l = {}, len(ring)
        for i, c in enumerate(ring):
            di.setdefault(c, []).append(i)
        print(di)

        prev, pc = [min(i, l-i) for i in di[key[0]]], key[0]
        print(f'prev = {prev}')
        for c in key[1:]:
            if c == pc:
                continue
            curr, k = [], 0
            for i in di[c]:
                if i < di[pc][0] or i > di[pc][-1]: 
                    r, s = 0, -1
                else:
                    while di[pc][k] < i:
                        k = k+1
                    r, s = k-1, k
                print(f'i = {i}, r = {r}, s = {s}, k = {k}, pc = {pc}, di[pc][k] = {di[pc][k]}')
                curr.append(min(prev[r]+abs(i-di[pc][r]), prev[r]+l-abs(i-di[pc][r]), prev[s]+abs(i-di[pc][s]), prev[s]+l-abs(i-di[pc][s])))
            prev, pc = curr, c
            print(f'prev = {prev}')
        return min(prev)+len(key)

sol = Solution()
import random
import string
ring = 'godding'
key = 'gd'
random.seed(46)
ring = ''.join(random.choices('abcdedfg', k=20))
key = ''.join(random.choices('abcdedfg', k=4))
print(f'ring = {ring}, key = {key}')
print(sol.findRotateSteps(ring, key))

