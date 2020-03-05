#!/usr/bin/env python

class Solution:
    def partialSum(self, candidates, partial, start):
        curr = candidates[start]
        print(f'start: {start}, partial: {partial}, curr: {curr}')
        if start >= len(candidates) or curr > partial:
            return []
        if curr == partial:
            return [[curr]]
        return [[curr] + i for i in self.partialSum(candidates, partial-curr, start+1)] + self.partialSum(candidates, partial, start+1) 

    def combinationSum2(self, candidates, target):
        return self.partialSum(sorted(candidates), target, 0)


candidates, target = [10,1,2,7,6,1,5], 8
sol = Solution()
print(sol.combinationSum2(candidates, target))
