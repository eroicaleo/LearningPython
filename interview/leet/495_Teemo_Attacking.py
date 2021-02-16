#!/usr/bin/env python3

class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        start = latest = ret = 0
        for t in timeSeries:
            if t > latest:
                ret += latest-start
                start = t
            latest = t+duration
        return ret+latest-start

timeSeries, duration = [1,4], 2
timeSeries, duration = [1,2], 2

sol = Solution()
print(sol.findPoisonedDuration(timeSeries, duration))
