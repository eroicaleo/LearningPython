#!/usr/bin/env python

class Solution:
    def combinationSum2(self, candidates, target):
        ret, candidates, l = [], sorted(candidates, reverse=True), len(candidates)
        def helper(start, t, prev):
            if t == 0:
                ret.append(prev)
                return
            if start == l:
                return
            for i in range(start, l):
                c = candidates[i] 
                if c <= t and (i == start or candidates[i] < candidates[i-1]):
                    helper(i+1, t-c, prev+[c])
        helper(0, target, [])
        return ret

candidates, target = [10,1,2,7,6,1,5], 8
candidates = [2,5,2,1,2]
target = 5
sol = Solution()
print(sol.combinationSum2(candidates, target))
