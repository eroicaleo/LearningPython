#!/usr/bin/env python3

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num, den = 1, 1
        for i in range(0, m-1):
            num *= (n+i)
            den *= (i+1)
        return num // den

    def uniquePaths2(self, m, n):
        return math.comb(m+n-2, n-1)

sol = Solution()
print(sol.uniquePaths(3, 2))
print(sol.uniquePaths(7, 3))
print(sol.uniquePaths(7, 1))
print(sol.uniquePaths(1, 7))
