#!/usr/bin/env python

from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        c1, l1, l2 = Counter(s1), len(s1), len(s2)
        lo, hi = 0, l1-1
        c2 = '' if l2 < l1 else Counter(c for c in s2[:l1] if c in c1)
        while hi < l2:
            print(f'lo = {lo}, hi = {hi}, c1 = {c1}, c2 = {c2}')
            if c1 == c2:
                return True
            if s2[lo] in c1:
                c2[s2[lo]] -= 1
            lo, hi = lo+1, hi+1
            if hi >= l2:
                break
            if s2[hi] in c1:
                c2[s2[hi]] += 1
        return False

s1 = 'ab'
s2 = 'eidbaooo'
s1 = 'ab'
s2 = 'eidboaoo'
s1 = 'eidboaoo'
s2 = 'ab'
sol = Solution()
print(sol.checkInclusion(s1, s2))
