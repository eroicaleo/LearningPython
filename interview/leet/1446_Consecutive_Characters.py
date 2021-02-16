#!/usr/bin/env python3

class Solution:
    def maxPower(self, s):
        p, cnt, ret = '', 1, 0
        for c in s:
            if c == p:
                cnt += 1
            else:
                ret, cnt = max(ret, cnt), 1
            p = c
        return max(ret, cnt)

str_list = [
    'cc',
    'leetcode',
    'abbcccddddeeeeedcba',
    'triplepillooooow',
    'hooraaaaaaaay',
    'tourist',
]

sol = Solution()
for s in str_list:
    print(s, sol.maxPower(s))
