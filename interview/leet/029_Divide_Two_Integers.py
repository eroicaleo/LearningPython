#!/usr/bin/env python

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n = 31
        quotient = 0
        flip = 1
        if dividend < 0:
            dividend = -dividend
            flip = -flip
        if divisor < 0:
            divisor = -divisor
            flip = -flip
        while n >= 0:
            print('n = %d' % n)
            d = divisor << n
            if dividend >= d:
                print('shift %d bits' % n)
                dividend -= d
                quotient += 1 << n
                print('new dividend: %d' % dividend)
            n -= 1
            if dividend < divisor:
                if flip < 0:
                    quotient = -quotient
                if quotient < -2147483648 or quotient > 2147483647:
                    quotient = 2147483647
                return quotient

sol = Solution()
dividend, divisor = 10, 3
dividend, divisor = 7, -3
dividend, divisor = 0, -3
dividend, divisor = 1, 1
dividend, divisor = -2147483648, -1
print(sol.divide(dividend, divisor))
