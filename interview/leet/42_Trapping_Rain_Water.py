#!/usr/bin/env python

class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        lo, hi, water, low = 0, len(height)-1, 0, 0
        while lo < hi:
            low = max(low, min(height[lo], height[hi]))
            if height[lo] <= height[hi]: lo, water = lo+1, water+(low-height[lo])
            else                       : hi, water = hi-1, water+(low-height[hi])
        return water

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))
