#!/usr/bin/env python3

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        queue, ret = deque(), []
        for i in range(len(nums)):
            while len(queue) > 0 and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            print(i, queue)
            if queue[0] <= i-k:
                queue.popleft()
            if i >= k-1:
                ret.append(nums[queue[0]])
            print(i, queue)
        return ret

nums, k = [1,3,-1,-3,5,3,6,7], 3
nums, k = [-7,-8,7,5,7,1,6,0], 4
nums, k = [], 0
sol = Solution()
wrong_anwser = sol.maxSlidingWindow(nums, k)
print(wrong_anwser)
