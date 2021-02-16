#!/usr/bin/env python3

class Solution:
    def sequentialDigits(self, low, high):
        ll, lh = len(str(low)), len(str(high))
        ret = []
        for l in range(ll, lh+1):
            for i in range(1, 11-l):
                print(f'i = {i}')
                d = 0
                for k in range(i, i+l):
                    d = d*10+k
                if low <= d <= high:
                    ret.append(d)
                elif d > high:
                    return ret
        return ret

sol = Solution()
low, high = 1000, 13000
low, high = 100, 300
low, high = 10, 1000
print(sol.sequentialDigits(low, high))
