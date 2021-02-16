#!/usr/bin/env python

import collections
from heapq import heappush, heappop

class Solution:
    def getLable(self, originalTag, limit):
        cnt = collections.Counter(originalTag)
        heap = []
        for k in cnt:
            heappush(heap, (-ord(k), k, cnt[k]))
        print(heap)
        prev, cont = '$', 0
        while heap:
            v0, c0, left0 = heappop(heap)
            if c0 == prev and cont == limit-1:

originalTag, limit = 'cbddd', 2
sol = Solution()
print(sol.getLable(originalTag, 2))
