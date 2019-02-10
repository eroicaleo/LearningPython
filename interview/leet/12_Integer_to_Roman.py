#!/usr/bin/env python

class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        divider, RomanDict, ret = 1000, {1: 'IVX', 10: 'XLC', 100: 'CDM', 1000: 'M'}, ''
        while divider > 0:
            quotient, divider, romanStr = num // divider, divider // 10, RomanDict[divider]
            if quotient == 0:
                continue
            if quotient < 4:
                ret += quotient * romanStr[0]
            elif quotient == 4:
                ret += romanStr[:2]
            elif quotient < 9:
                ret += romanStr[1] + romanStr[0] * (quotient-5)
            else:
                ret += romanStr[0] + romanStr[2]
            num -= quotient * divider * 10
        return ret

sol = Solution()
print(sol.intToRoman(3999))
print(sol.intToRoman(2034))
print(sol.intToRoman(2000))

