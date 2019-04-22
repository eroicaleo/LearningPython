#!/usr/bin/env python

class Solution:
    def reverseWords(self, s):
        return ' '.join(s.strip().split()[::-1])

sol = Solution()
s = '  hello world!  '
s = 'a good    example'
print(sol.reverseWords(s))
