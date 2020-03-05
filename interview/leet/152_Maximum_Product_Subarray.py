#!/usr/bin/env python

class Solution:
    def maxProduct(self, nums):
        sign, prod = [-1]*len(nums), [0]*len(nums)
        p, maxProd = 1, nums[0]
        for i, n in enumerate(nums):
            p *= n
            prod[i] = p
            if n < 0 and p < 0:
                sign[i] = i
            elif n > 0 and p < 0:
                sign[i] = sign[i-1]

            if sign[i] == -1:
                maxProd = max(maxProd, p)
            elif sign[i] != i:
                maxProd = max(maxProd, p//prod[sign[i]])

            if p == 0:
                p = 1

        print(sign)
        print(prod)
        return maxProd

sol = Solution()
nums = [2,3,-5,-4,-3,500,0,2,4]
nums = [2,3,-1,2]
nums = [-1,2,3]
nums = [-1,0,-2]
print(nums)
print(sol.maxProduct(nums))
