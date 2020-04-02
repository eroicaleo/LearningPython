#!/usr/bin/env python3

# Thinking process
# The order of robbing doesn't matter
# So we can think robbing from low to high
# what is the row: the house in it's door number
# what is the col: the ith robbery
# what is the meaning of dp[i, j]: the max money can get after jth robbery and the robbered house number is <= i
# what is recurrance relation dp[i, j] = max(dp[i-1, j], dp[i-2, j-1]+nums[i], dp[i,j-1])
# Here we divided dp[i, j] into 3 disjoint categories:
#   1. house i has been robbed in previous round, so it's dp[i,j-1]
#   2. we don't rob house i in round j, i.e. dp[i-1, j]
#   3. we rob house i in round j, i.e. dp[i-2, j-1]+nums[i]

# Other points: how to avoid robbing house 0 and house l-1
# I don't have better method and have to do it in 2 rounds
# 1. we don't rob house 0
# 1. we don't rob house l-1

class Solution:
    def rob(self, nums):
        l = len(nums)
        if l <= 2:
            return max(nums)
        print('#'*80)
        print(f'do not rob house {l-1}')
        print('#'*80)
        dp_last, dp_curr = [0]*l, [0]*l
        for k in range((l-1)//2):
            print(f'k = {k}, dp_last = {dp_last}')
            for i in range(2*k, l-1):
                dp_curr[i] = max(dp_last[i], dp_curr[i-1] if i>0 else 0, dp_last[i-2]+nums[i])
            print(f'k = {k}, dp_curr = {dp_curr}')
            dp_last, dp_curr = dp_curr, [0]*l
        r1 = dp_last[-2]
        print('#'*80)
        print('do not rob house 0')
        print('#'*80)
        nums[0] = 0
        dp_last, dp_curr = [0]*l, [0]*l
        for k in range(l//2):
            print(f'k = {k}, dp_last = {dp_last}')
            for i in range(2*k, l):
                dp_curr[i] = max(dp_last[i], dp_curr[i-1] if i>0 else 0, dp_last[i-2]+nums[i])
            print(f'k = {k}, dp_curr = {dp_curr}')
            dp_last, dp_curr = dp_curr, [0]*l
        r2 = dp_last[-1]
        return max(r1, r2)
 
sol = Solution()
nums = [2,3,2]
nums = [1,2,3,1]
nums = [5,4,3,2,1,6,7,20,2]
nums = [3,2]
nums = [35,4,3,2,1,6,7,20,36]
print(sol.rob(nums))

