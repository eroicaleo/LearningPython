#!/usr/bin/env python3

import collections

class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        queue = collections.deque([(0, 0, poured)])
        d = {}
        while queue:
            r, g, p = queue.popleft()
            print(f'r = {r}, g = {g}, p = {p}')
            if query_row < r or (query_row == r and query_glass < g):
                break
            curr = d.setdefault((r, g), 0)
            new_drop = min(p, (1-curr))
            d[(r, g)] += new_drop
            p -= new_drop
            if p > 0:
                queue.append((r+1, g,   p/2))
                queue.append((r+1, g+1, p/2))
        return d.get((query_row, query_glass), 0)

    def champagneTower(self, poured, query_row, query_glass):
        glasses = [poured]
        for r in range(1,query_row+1):
            new_glasses = [0]*(r+1)
            new_glasses[0] = new_glasses[-1] = max(glasses[0]-1.0, 0.0)/2
            for g in range(1, r):
                new_glasses[g] = max((glasses[g-1]-1.0), 0.0)/2 + max((glasses[g]-1.0), 0.0)/2
            glasses = new_glasses
            # print(f'row = {r}', glasses)
        return min(glasses[query_glass], 1.0)

# (10000000009, 33, 17)
sol = Solution()
info = [
(1,1,1),
(2,1,1),
(4,2,2),
(10000000009, 33, 17),
]
for poured, query_row, query_glass in info:
    print(poured, query_row, query_glass, sol.champagneTower(poured, query_row, query_glass))
