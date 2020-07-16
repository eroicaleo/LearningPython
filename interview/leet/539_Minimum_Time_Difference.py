#!/usr/bin/env python

import random

class Solution:
    def findMinDifference(self, timePoints) -> int:
        def s2t(s):
            hr, mi = s.split(':')
            return int(hr)*60+int(mi)
        timePoints = sorted(map(s2t, timePoints))
        timePoints.append(timePoints[0]+1440)
        return min([b-a for a, b in zip(timePoints, timePoints[1:])])

timePoints = []
for i in range(10):
    hr, mi = random.choice(range(24)), random.choice(range(60))
    timePoints.append(f'{hr:02d}:{mi:02d}')
print(timePoints)

timePoints = ['23:59', '00:00']
timePoints = ['05:31', '22:08', '00:35']
sol = Solution()
print(sol.findMinDifference(timePoints))
