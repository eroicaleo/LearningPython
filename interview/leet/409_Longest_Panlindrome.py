#!/usr/bin/env python

from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        cnt = Counter(s)
        l, odd = 0, 0
        for k, n in cnt.items():
            if n % 2 == 0:
                l += n
            else:
                l += (n-1)
                odd = 1
        return l+odd

slist = [
    'abccccdd',
    'abbccccdd',
    ]
sol = Solution()
for s in slist:
    print(f's = {s}, {sol.longestPalindrome(s)}')

