#!/usr/bin/env python3

class Solution:
    def removeStones(self, stones):
        parent, size, dy, self.n = {}, {}, {}, 0
        def union(v, w):
            print(f'union {v} and {w}')
            rootv, rootw = root(v), root(w)
            if rootv == rootw:
                return
            self.n -= 1
            if size[rootv] < size[rootw]: 
                rootv, rootw = rootw, rootv
            parent[rootw], size[rootv], size[rootw] = rootv, size[rootv]+size[rootw], 0
            print(f'after union parent = {parent}, size = {size}')
        def root(v):
            print(f'find root of {v}, ', end='')
            while parent[v] != v:
                parent[v], v = parent[parent[v]], parent[v]
            print(f'It\'s {v}')
            return v
        for x, y in stones:
            print(f'x = {x}, y = {y}')
            # d.setdefault(x, set()).add(y)
            if not x in parent:
                parent[x] = x
                size[x] = 1
                self.n += 1
            if y in dy:
                union(x, dy[y])
            else:
                dy[y] = x
            # dy.setdefault(y, set()).add(x)
            print(f'dy = {dy}')
        return len(stones)-self.n

stones = [[0,0]]
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
sol = Solution()
print(sol.removeStones(stones))
