#!/usr/bin/env python

class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        ret, length = '', len(s)
        for i, c in enumerate(s):
            j = 0
            while j <= i < length-j and s[i-j] == s[i+j]:
                j += 1
            j -= 1
            if len(ret) < 2*j+1:
                ret = s[i-j:i+j+1]
            j = 0
            while j <= i < length-j-1 and s[i-j] == s[i+1+j]:
                j += 1
            if len(ret) < 2*j:
                ret = s[i-j+1:i+j+1]
        return ret

sol = Solution()
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('cbbd'))
