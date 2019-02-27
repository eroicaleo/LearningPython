#!/usr/bin/env python

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack, length, maxarea, heights = [-1], len(heights)+1, 0, heights+[-1]
        for i in range(length):
            while heights[stack[-1]] > heights[i]:
                maxarea = max(heights[stack.pop(-1)] * (i-stack[-1]-1), maxarea)
            if heights[stack[-1]] < heights[i]: stack.append(i)
            # stack.append(i)
            print(stack)
        return maxarea

sol = Solution()
heights = list(range(20000))
heights = [2,1,5,6,2,3]
heights = []
heights = [0,9]
print(sol.largestRectangleArea(heights))
