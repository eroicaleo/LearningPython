#!/usr/bin/env python3

class Solution:
    def isHappy(self, n):
        dic = dict()
        while (n not in dic) and (n != 1):
            k, dic[n] = 0, 1
            print(f'before n = {n}')
            while n > 0:
                n, k = (n//10), k+(n%10)**2
            n = k
            print(f'after n = {n}')
        return n == 1

sol = Solution()
n = 19
n = 4
print(sol.isHappy(n))
