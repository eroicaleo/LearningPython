#!/usr/bin/env python

class Solution:
    def subarraySum(self, nums, k):
        from collections import deque
        s, d, ret = 0, {}, 0
        for i, n in enumerate(nums):
            s += n
            if s in d:
                d[s].append(i)
            else:
                d[s] = deque([i])
            if s == k:
                ret += 1
        for i, n in enumerate(nums):
            k += n
            if k in d:
                while len(d[k]) > 0 and (d[k][0] <= i):
                    d[k].popleft()
                ret += len(d[k])
            print('k, i, n, ret, d:', k, i, n, ret, d)
        return ret

sol = Solution()
nums, k = [1], 0
nums, k = [1,1,1], 2
nums, k = [1,1,1,1], 2
nums, k = [0]*10, 0
nums, k = [-1,-1,1], 0 
print(sol.subarraySum(nums, k))
