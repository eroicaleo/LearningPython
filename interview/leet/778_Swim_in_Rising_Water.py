#!/usr/bin/env python3

# Thinking process
# The animation of spanning with colors black/white/gray
# Like the ones in princeton lecture really helped me

from heapq import heappush, heappop
class Solution:
    def swimInWater(self, grid):
        l, heap, delta = len(grid), [(grid[0][0], 0, 0)], [(0,1),(0,-1),(1,0),(-1,0)]
        for t in range(l**2):
            while heap[0][0] <= t:
                v, i, j = heappop(heap)
                if i == j == l-1:
                    return t
                for dx, dy in delta:
                    x, y = i+dx, j+dy
                    if 0 <= x < l and 0 <= y < l and grid[x][y] >= 0:
                        heappush(heap, (grid[x][y], x, y))
                grid[i][j] = -1
            print('#'*80)
            print(f'After time {t}:')
            print(f'heap = {heap}')
            for g in grid:
                print(' '.join(map(lambda d: f'{d:-2d}', g)))

sol = Solution()
grid = [[0,2],[1,3]]
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
grid = [[24,1,2,3,4],[0,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

print(sol.swimInWater(grid))
