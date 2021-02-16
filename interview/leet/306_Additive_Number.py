#!/usr/bin/env python3

class Solution:
    def isAdditiveNumber(self, num):
        l = len(num)
        for i in range(l//2):
            a0 = int(num[:i+1])
            for j in range(i+1, min(i+1+l//2, l-1)):
                a1 = int(num[i+1:j+1])
                print(f'a0 = {a0}, a1 = {a1}')
                s = str(a0)+str(a1)
                while len(s) < l:
                    if not num.startswith(s):
                        break
                    s, a0, a1 = s+str(a0+a1), a1, a0+a1
                print(s)
                if s == num:
                    return True
                a0 = int(num[:i+1])
        return False


num = '123'
num = '10'
num = '112358'
num = '199100199'

sol = Solution()
print(sol.isAdditiveNumber(num))

