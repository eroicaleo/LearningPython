#!/usr/bin/env python3

import itertools

class Solution:
    def largestTimeFromDigits(self, A):
        for p in sorted(itertools.permutations(A), reverse=True):
            if 10*p[0]+p[1]<24 and 10*p[2]+p[3]<60:
                return f'{p[0]}{p[1]}:{p[2]}{p[3]}'
        return ""

    def largestTimeFromDigits_2(self, A):
        pass

A = [1,2,3,4]
A = [5,5,5,5]
sol = Solution()
print(sol.largestTimeFromDigits(A))
