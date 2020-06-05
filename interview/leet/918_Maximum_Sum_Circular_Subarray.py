#!/usr/bin/env python

import math
class Solution:
    def maxSubarraySumCircular(self, A):
        presum = A[0]
        sum_max = presum_max = -math.inf
        sum_min = presum_min = math.inf
        for a in A[1:]:
            presum_min = min(presum, presum_min)
            presum_max = max(presum, presum_max)
            presum += a
            sum_max = max(sum_max, presum, presum-presum_min)
            sum_min = min(sum_min, presum, presum-presum_max)
            print(f'presum = {presum}, presum_min = {presum_min}, presum_max = {presum_max}')
            print(f'sum_max = {sum_max}, sum_min = {sum_min}')
        return sum_max if presum==sum_min else max(presum-sum_min, sum_max)

A = [5,-3,5]
A = [1,-2,3,-2]
A = [3,-1,2,-1]
A = [3,-2,2,-3]
A = [1,2,3]
A = [-2,-3,-1]
sol = Solution()
print(sol.maxSubarraySumCircular(A))
