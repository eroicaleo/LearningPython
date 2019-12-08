#!/usr/bin/env python3

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[]] + [[] for i in range(target)]
        for i, c in enumerate(candidates):
            for j in range(c, target+1):
                # if dp[j-c]:
                    dp[j] += ([l+[c] for l in dp[j-c]] + ([[c]] if j == c else []))
                # elif j == c:
                #     dp[j] += [[c]]
            print('c = ', c, dp)
        return dp[-1]

sol = Solution()
candidates, target = [2,3,6,7], 1
candidates, target = [], 0
candidates, target = [2,3,6,7], 7
candidates, target = [2,3,5], 8
print(sol.combinationSum(candidates, target))
