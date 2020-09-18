#!/usr/bin/env python3

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker): 
        worker, i = sorted(worker, reverse=True), 0
        l, ret = len(worker), 0
        for p, d in sorted(zip(profit, difficulty), reverse=True):
            while i < l and worker[i] >= d:
                ret, i = ret+p, i+1
        return ret

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

sol = Solution()
print(sol.maxProfitAssignment(difficulty, profit, worker))
