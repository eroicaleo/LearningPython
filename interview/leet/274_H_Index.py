#!/usr/bin/env python

import collections

class Solution:
    def hIndex(self, citations) -> int:
        cnt = collections.Counter(citations)
        h_index, above = 0, len(citations)
        for i in sorted(cnt):
            print(f'i = {i}, cnt[i] = {cnt[i]}, above = {above}')
            if above >= h_index:
                h_index = i
            above -= cnt[i]
        return h_index

sol = Solution()
citations = [3,0,6,1,5]
print(sol.hIndex(citations))
