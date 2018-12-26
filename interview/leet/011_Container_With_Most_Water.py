#!/usr/bin/env python

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        l, r = height[i], height[j]
        maxArea = (j - i) * min(l, r)
        while j > i:
            if l < r:
                while height[i] <= l:
                    i += 1
            elif r < l:
                while height[j] <= r:
                    j -= 1
            else:
                i, j = i+1, j-1
            l, r = height[i], height[j]
            print(i, j, l, r)
            area = (j - i) * min(l, r)
            if area > maxArea:
                maxArea = area
        return maxArea

sol = Solution()
height_list = [
[1,8,6,2,5,4,8,3,7],
[1,2],
[1,2,4,3],
[2,3,4,5,18,17,6],
]
for height in height_list:
    print(sol.maxArea(height))
