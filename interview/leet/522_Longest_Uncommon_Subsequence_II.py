#!/usr/bin/env python3

import collections
class Solution:
    def findLUSlength(self, strs):
        cnt = collections.Counter(strs)
        unique_strs = sorted([s for s in cnt if cnt[s] == 1], key=len, reverse=True)
        print(unique_strs)

        def isSubSeq(s1, s2):
            if len(s1) > len(s2):
                return False
            prev, curr = [0]*(1+len(s2)), [0]*(1+len(s2))
            for c1 in s1:
                for i, c2 in enumerate(s2):
                    curr[i+1] = prev[i]+1 if c1 == c2 else max(prev[i+1], curr[i])
                prev, curr = curr, [0]*(1+len(s2))
                # print(prev)
            return prev[-1] == len(s1)

        def isSubSeq2(s1, s2):
            i = 0
            for c2 in s2:
                i += 1 if s1[i] == c2 else 0
            return i == len(s1)

        non_unique_strs = sorted([s for s in cnt if cnt[s] > 1], key=len, reverse=True)
        for us in unique_strs:
            if all(not isSubSeq2(us, nus) for nus in non_unique_strs):
                print(us)
                return len(us)
        return -1

sol = Solution()
strs = ["aba", "cdc", "eae"]
strs = ["aba", "cdc", "eae", "aba", 'cdc', 'eae', 'eb', 'ec', 'ed', 'f', 'q']
strs = ["aba", 'aba']
print(sol.findLUSlength(strs))


