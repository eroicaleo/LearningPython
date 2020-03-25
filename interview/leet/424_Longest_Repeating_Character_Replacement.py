#!/usr/bin/env python

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = '' if not s else Counter(s[0])
        lo = hi = maxlen = 0
        while hi < len(s):
            while hi-lo-c.most_common()[0][1] < k:
                hi = hi+1
                maxlen = max(maxlen, hi-lo)
                if hi == len(s):
                    break
                c[s[hi]] += 1
                print(f'hi = {hi}, lo = {lo}, c = {c.most_common()}, maxlen = {maxlen}')
            c[s[lo]], lo = c[s[lo]]-1, lo+1
            print(f'hi = {hi}, lo = {lo}, c = {c}, maxlen = {maxlen}')
        return maxlen

s = "ABAB"
k = 2

s = "AABABBA"
k = 1

s = "AAAAAA"
k = 0

s = ""
k = 1

s = "ABCDE"
k = 10

sol = Solution()
print(sol.characterReplacement(s, k))
