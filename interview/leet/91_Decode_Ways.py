#!/usr/bin/env python

class Solution:
    def numDecodings(self, s):
        if len(s) > 0 and s[0] == '0':
            return 0
        elif len(s) < 2:
            return 1
        else:
            return self.numDecodings(s[1:]) + (0 if int(s[:2]) > 26 else self.numDecodings(s[2:]))

sol = Solution()
s = '1'
s = '12'
s = '123'
s = '226'
s = '305'
print(sol.numDecodings(s))
