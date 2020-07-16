#!/usr/bin/env python3

# 473. Matchsticks to Square
# Medium

# 563

# 59

# Add to List

# Share
# Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

# Example 1:
# Input: [1,1,2,2,2]
# Output: true

# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:
# Input: [3,3,3,3,4]
# Output: false

# Explanation: You cannot find a way to form a square with all the matchsticks.
# Note:
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.

class Solution:
    def makesquare(self, nums) -> bool:
        s = sum(nums)
        if s % 4 > 0:
            return False
        l = sum(nums) // 4
        self.sticks, self.edges, self.res = [0]*16, [l]*4, False
        for n in nums:
            self.sticks[n] += 1
        def dfs(ub):
            if sum(self.edges) == 0:
                return True
            for i in range(4):
                if self.edges[i] > 0:
                    break
            for s in range(15,0,-1):
                if self.sticks[s] > 0 and s <= self.edges[i]:
                    self.sticks[s] -= 1
                    self.edges[i] -= s
                    if dfs(s):
                        return True
                    self.sticks[s] += 1
                    self.edges[i] += s
            return False
        return dfs(15)

nums = [1,1,2,2,2]
nums = [3,3,3,3,4]
nums = [1,1,1,1,4,4,4,4]
sol = Solution()
print(sol.makesquare(nums))
test_list = [0,0,0,0]
# print(next(i for i, n in enumerate(test_list) if n > 0))
