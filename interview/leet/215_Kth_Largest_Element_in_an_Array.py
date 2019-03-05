#!/usr/bin/env python

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        from heapq import heappush, heappushpop
        heap = []
        for i, c in enumerate(nums):
            m = heappush(heap, nums[i]) if i < k else heappushpop(heap, nums[i])
        return heap[0]

sol = Solution()
nums, k = [3,2,1,5,6,4], 2
nums, k = [3,2,3,1,2,4,5,5,6], 4
print(sol.findKthLargest(nums, k))
