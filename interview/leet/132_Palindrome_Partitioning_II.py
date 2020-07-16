#!/usr/bin/env python

class Solution:
    def minCut(self, s):
        def isP(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1; j -= 1
            return True
        l, k = len(s), 0
        prev, curr = [1]+[0]*l, [0]*(1+l)
        for k in range(l):
            for i, cut in enumerate(prev):
                if cut:
                    for j in range(i+1, l+1):
                        print(f'{i}, {j}')
                        if isP(i, j-1):
                            curr[j] = 1
            prev, curr = curr, [0]*(1+l)
            print(f'{prev}')
            if prev[-1]:
                break
        return k
            

s = 'aab'
s = 'abcbad'
s = 'aaa'
s = ''
sol = Solution()
print(sol.minCut(s))
