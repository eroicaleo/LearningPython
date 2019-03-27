#!/usr/bin/env python

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        tdict, lo, hi, sdict, length, ret = defaultdict(int), 0, 0, defaultdict(int), len(s), ''
        for c in t:
            tdict[c] += 1
        def compareStrDict(s, t):
            for k in t:
                if s[k] < t[k]:
                    return -1
            return 1
        while hi < length and t != '':
            while hi < length and compareStrDict(sdict, tdict) < 0:
                c, hi = s[hi], hi+1
                if c in t:
                    sdict[c] += 1
            if compareStrDict(sdict, tdict) < 0:
                break
            while compareStrDict(sdict, tdict) > 0:
                c, lo = s[lo], lo+1
                if c in t:
                    sdict[c] -= 1
            if ret == '' or len(ret) > (hi-lo)+1:
                ret = s[lo-1:hi]
        return ret

S, T = "", "ABCX"
S, T = "ADOBECODEBANC", ""
S, T = "ADOBECODEBANC", "ABC"
S, T = "ADOBECODEBANC", "ABCX"
S, T = "A", "AA"
sol = Solution()
print(sol.minWindow(S, T))
