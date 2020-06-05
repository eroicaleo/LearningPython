#!/usr/bin/env python3

# Thinking Process
# 

from heapq import heappush, heappop
class Solution:
    def medianSlidingWindow(self, nums, k):
        heapl, heaph, d = [], [], {}
        sizel, sizer = 0, 0
        for i, n in enumerate(nums):
            print('#'*80)
            print(f'i = {i}, n = {n}')
            # push
            heappush(heapl, -n)
            sizel += 1
            if sizel > k//2:
                heappush(heaph, -heappop(heapl))
                sizel, sizer = sizel-1, sizer+1
            print(f'heapl = {heapl}')
            print(f'heaph = {heaph}')
            # pop
            if i >= k:
                j = nums[i-k]
                print(f'j = {j}')
                d[j] = d.get(j, 0) + 1
                print(f'd = {d}, heaph[0] = {heaph[0]}')
                if -heapl[0] >= j:
                    while heapl and d.get(-heapl[0], 0) > 0:
                        d[-heappop(heapl)] -= 1
                    heappush(heapl, -heappop(heaph))
                else:
                    while heaph and d.get(heaph[0], 0) > 0:
                        d[heappop(heaph)] -= 1
                sizer -= 1
            print(f'After')
            print(f'd = {d}')
            print(f'heapl = {heapl}')
            print(f'heaph = {heaph}')
            print(f'sizel = {sizel}, sizer = {sizer}')

sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.medianSlidingWindow(nums, k))
