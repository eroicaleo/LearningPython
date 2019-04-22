#!/usr/bin/env python

class Solution:
    def longestValidParentheses(self, s):
        accum, maxlen = 0, 0
        for i in range(len(s)):
            accum = 0
            for j in range(i, len(s)):
                accum += 1 if s[j] == '(' else -1
                print('i, j, accum', i, j, accum)
                if accum < 0:
                    break
                if accum == 0:
                    maxlen = max(maxlen, j-i+1)
        return maxlen

sol = Solution()
s = '(()'
s = ')()())'
print(sol.longestValidParentheses(s))
