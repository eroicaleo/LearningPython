#!/usr/bin/env python

import math

class Solution:
    def countArrangement(self, n):
        self.d = {(0,0):1}
        def dfs(i, j, prefix=''):
            print(f'{prefix}i = {i}, j = {j}')
            if (i, j) in self.d:
                return self.d[(i,j)]
            ret = 0
            k = (i & -i)
            p = int(math.log2(k))
            print(f'{prefix}p = {p}, k = {k}')
            for q in range(1, 16):
                if (j & (2**q)) and (p%q==0 or q%p==0):
                    ret += dfs(i^k, j^(2**q), prefix+'  ')
            self.d[(i,j)] = self.d[(j,i)] = ret
            print(f'{prefix}ret = {ret}')
            return ret
        k = sum(2**i for i in range(1,n+1))
        return dfs(k, k)
                        

sol = Solution()
print(sol.countArrangement(4))
