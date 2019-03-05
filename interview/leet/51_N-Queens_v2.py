#!/usr/bin/env python

class Solution:
    def solveNQueens(self, n: int):
        import itertools
        def search(seq, col, dia1, dia2, k):
            return [seq] if k == n else list(itertools.chain.from_iterable([search(seq+str(i), col+[i], dia1+[k+i], dia2+[k-i], k+1) for i in range(n) if (i not in col) and (k+i not in dia1) and (k-i not in dia2)]))
        return [["."*int(c) + "Q" + "."*(n-int(c)-1) for c in b] for b in search('', [], [], [], 0)]

sol = Solution()
print(sol.solveNQueens(5))
                    
# print('k = %d, seq = %s, col = %s, dia1 = %s, dia2 = %s' % (k, seq, col, dia1, dia2))
