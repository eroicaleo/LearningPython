#!/usr/bin/env python3

import string


class Solution:
    def uniqueLetterString(self, s):
        d1, d2 = {c: -1 for c in string.ascii_uppercase}, {c: -1 for c in string.ascii_uppercase}
        ret, last = 0, 0
        for i, c in enumerate(s):
            last = last + (i-1) + d2[c] - 2*d1[c] + 1
            print(f'i = {i}, c = {c}, last = {last}')
            ret += last
            d1[c], d2[c] = i, d1[c]
        return ret

sol = Solution()
s = 'LEETCODE'
s = 'ABA'
s = 'ABC'
print(sol.uniqueLetterString(s))
