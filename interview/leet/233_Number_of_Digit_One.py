#!/usr/bin/env python

class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        num, numNew = n, n
        bitLen = 10
        p = [0] * bitLen
        a = [0] * bitLen
        ret = 0
        for n in range(1, bitLen):
            p[n] = 10 ** (n-1) + 10 * p[n-1]
        # print(p)
        n = 0
        while num > 0:
            a[n] = num % 10
            num = (num - a[n]) // 10
            n += 1
        # print(a)
        n -= 1
        while n >= 0 and numNew > 0:
            if a[n] == 0:
                n -= 1
                continue
            ret += a[n] * p[n]
            numNew -= a[n] * 10 ** n
            if a[n] == 1:
                ret += (numNew + 1)
            else:
                ret += 10 ** n
            n -= 1
        return ret

sol = Solution()
for i in range(0, 1112):
    print(i, sol.countDigitOne(i))
