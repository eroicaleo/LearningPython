#!/usr/bin/env python3

from heapq import heappush, heappop
class Solution:
    def isPossible(self, nums):
        heap = [(nums[0], 1)]
        for n in nums[1:]:
            if n == heap[0][0]:
                heappush(heap, (n, 1))
            else:
                while heap and heap[0][0] < n-1:
                    if heappop(heap)[1] < 3:
                        return False
                heappush(heap, (n, heappop(heap)[1]+1 if heap else 1))
            print(f'heap = {heap}')
        return all(h[1] >= 3 for h in heap)

sol = Solution()
nums = [1,2,3,3,4,5]
nums = [1,2,3,3,4,5,9,10,11]
nums = [1,2,3,3,4,4,5,5]
nums = [1,2,3,4,4,5]
print(sol.isPossible(nums))

