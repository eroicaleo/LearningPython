#!/usr/bin/env python3

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1
        if numerator < 0:
            sign *= -1
        if denominator < 0:
            sign *= -1
        numerator, denominator = abs(numerator), abs(denominator)
        p, r = numerator//denominator, 10*(numerator%denominator)
        if r == 0:
            return str(sign*p)
        decimal, d, pos = '', {0:1}, 0
        while True:
            # r = r*10
            while r < denominator and (not r in d):
                d[r], r, decimal, pos = pos, r*10, decimal+'0', pos+1
            if r in d:
                break
            print('d, r, pos = ', d, r, pos)
            d[r], pos = pos, pos+1
            q, r = r//denominator, 10*(r%denominator)
            decimal += str(q)
        if r:
            decimal = decimal[:d[r]] + '('+decimal[d[r]:]+')'
        ret = '%s.%s' % (str(p), str(decimal))
        if sign == -1:
            ret = '-' + ret
        return ret

sol = Solution()
for numerator, denominator in [
        (2, 3),
        (1, 2),
        (1, 4),
        (4, 333),
        (1, 7),
        (1, 6),
        (1, 90),
        (2, 1),
        (-50, 8),
        (7, -12),
        (-7, 12),
        ]:
    print(numerator, denominator, sol.fractionToDecimal(numerator, denominator))

print(-50%8)
print(-50%-8)
