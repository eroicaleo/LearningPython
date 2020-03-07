#!/usr/bin/env python

class Solution:
    def minSubArrayLen(self, s, nums) -> int:
        head, tail, l = 0, 0, len(nums)
        ret, partial = l+1, 0
        while tail < l:
            while tail < l and partial < s:
                partial += nums[tail]
                tail += 1
            while partial >= s:
                ret = min(tail-head, ret)
                partial -= nums[head]
                head += 1
            print(f'head: {head-1}, tail: {tail-1}, ret: {ret}')
        return 0 if ret == (l+1) else ret


nums = []
nums = [2,3,1,2,4,3]
s = 7
s = 8
s = 10
s = 100
nums = [1,2]
s = 3
sol = Solution()
print(sol.minSubArrayLen(s, nums))
