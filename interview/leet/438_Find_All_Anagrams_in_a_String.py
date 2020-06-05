#!/usr/bin/env python

import collections
class Solution:
    def findAnagrams(self, s, p):
        cnt, l = collections.Counter(p), len(p)
        lo, hi, ret = 0, 0, []
        for hi, c in enumerate(s):
            cnt[c] -= 1
            print(f'hi = {hi}, lo = {lo}, c = {c}, cnt = {cnt}')
            while cnt[c] < 0:
                cnt[s[lo]] += 1
                lo += 1
            if hi-lo == l-1:
                ret.append(lo)
        return ret

sol = Solution()
s, p = 'abab', 'ab'
s, p = 'cbaebabacd', 'abc'
print(sol.findAnagrams(s, p))
