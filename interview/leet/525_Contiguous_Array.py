#!/usr/bin/env python3

class Solution:
    def findMaxLength(self, nums):
        d, s, max_len = {0:-1}, 0, 0
        for i, n in enumerate(nums):
            s += (-1 if n == 0 else 1)
            d.setdefault(s, i)
            max_len = max(max_len, i-d[s])
        return max_len

    def findMaxLength_Stephan(self, nums):
        d, s, max_len = {0:-1}, 0, 0
        for i, n in enumerate(nums):
            s += n-0.5
            d.setdefault(s, i)
            max_len = max(max_len, i-d[s])
        return max_len

    def findMaxLength_Stephan_OneLiner(self, nums):
        return reduce(lambda(f,b,m),(i,x):(f,b+x-.5,max(m,i-f.setdefault(b+x-.5,i))),enumerate(nums),({0:-1},0,0))[2]

nums = [1,0]
nums = []
nums = [1,1,1]
nums = [1,0,1,0,1,0,1,0,1,1,1,1,1,1]
nums = [0]
nums = [1,0,1]
sol = Solution()
print(sol.findMaxLength_Stephan(nums))
