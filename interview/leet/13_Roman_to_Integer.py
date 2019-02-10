#!/usr/bin/env python

class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        romanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prevDict =  {'I':'', 'V':'I', 'X':'I', 'L':'X', 'C':'X', 'D':'C', 'M':'C'}
        ret = 0
        for i, c in enumerate(s):
            ret += romanDict[c]
            if i > 0 and s[i-1] == prevDict[c]:
                ret -= 2 * romanDict[s[i-1]]
        return ret

sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("IX"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
