#!/usr/bin/env python

# The v2 version is different from v1 in the sense
# It is count 1 in column fashion, while v1 counts 1 in row fashion.
# The main idea is, when 1 appears in the bit0, every 10 number it happens once
# when 1 appears in the bit1, every 100 number it happens 10 times and so on.

class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret, i = 0, 1
        while i <= n:
            j = 10 * i
            a, b = n // j, n % j
            ret += a * i
            c = b // i
            # print('a, b, c, i, j = %d, %d, %d, %d, %d' % (a, b, c, i, j))
            if c == 1:
                ret += (b - i + 1)
            elif c > 1:
                ret += i
            i = j
        return ret
 
sol = Solution()
for i in range(0, 112):
    print(i, sol.countDigitOne(i))

