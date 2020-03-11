#!/usr/bin/env python3

'''
The following thinking process helped me to get this approach
I image the real line, and I put the data in the list on the real line
I also give them different color.
An interval is like a bag, the bag is moving right along the real line
it can become bigger or small, but at any given time, it needs to have
all the colors in it.

heap status:
0, 4, 5
pop 0, push 9
range = [0, 5]
4, 5, 9
pop 4, push 10
range = [4, 9]
5, 9, 10
pop 5, push 18
9, 10, 18
range = [9, 18]
'''

from heapq import heappush, heappop

class Solution:
    def smallestRange(self, nums):
        heap, ub = [], nums[0][0]
        for k, l in enumerate(nums):
            heappush(heap, (l[0], k, 0))
            ub = max(l[0], ub)
        s_range = [heap[0][0], ub]
        print(f's_range = {s_range}, heap = {heap}')
        while True:
            _, k, i = heappop(heap)
            if i+1 >= len(nums[k]):
                break
            ub = max(nums[k][i+1], ub)
            heappush(heap, (nums[k][i+1], k, i+1))
            c_range = [heap[0][0], ub]
            if (((c_range[1] - c_range[0]) < (s_range[1] - s_range[0])) or
               (((c_range[1] - c_range[0]) == (s_range[1] - s_range[0])) and (c_range[0] < s_range[0]))):
                s_range = c_range
            print(f's_range = {s_range}, c_range = {c_range}, heap = {heap}')
        return s_range


nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
sol = Solution()
print(sol.smallestRange(nums))
# Output: [20,24]
