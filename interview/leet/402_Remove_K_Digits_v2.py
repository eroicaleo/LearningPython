#!/usr/bin/env python3

class Solution(object):
    def removeKdigits(self, num, k):
        r = ''
        for i, c in enumerate(num):
            print(f'outside while k = {k}, r = {r}')
            while k and r and c < r[-1]:
                k -= 1
                r = r[:-1]
                print(f'k = {k}, r = {r}')
            if r or c != '0':
                r += c
            # r = r.lstrip('0')
            if k == 0:
                return (r+num[i+1:]) or '0'
        # r = (r+num[i:]).lstrip('0')
        return '0' if k >= len(r) else r[:-k]

num = '1234567890'
k = 9
num = '1432219'
k = 3
num = '102030'
k = 2
num = '123456'
k = 7
num = '10'
k = 2
num = '1432219'
k = 0
num = ''
k = 1
sol = Solution()
print(sol.removeKdigits(num, k))
stack = [1,2,3,4,5]
print(stack[:-0 or None])
