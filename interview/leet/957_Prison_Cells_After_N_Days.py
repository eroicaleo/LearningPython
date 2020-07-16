#!/usr/bin/env python3

class Solution:
    def prisonAfterNDays(self, cells, N):
        self.cells = cells
        key = ''.join(map(str, cells))
        d, l = {}, []
        def next_key():
            new_cells = [0]*8
            for i in range(1,7):
                new_cells[i] = 1-(self.cells[i-1]+self.cells[i+1])%2
            self.cells = new_cells
            return ''.join(map(str, self.cells))
        for i in range(1+N):
            print(self.cells, key)
            if key in d:
                break
            d[key] = len(l)
            l.append(key)
            key = next_key()
        return l[-1] if not key in d else l[d[key]+(N-d[key])%(i-d[key])]

cells = [0,1,0,1,1,0,0,1]
N = 7
cells = [1,0,0,1,0,0,1,0]
N = 1000000000
sol = Solution()
print(sol.prisonAfterNDays(cells, N))

