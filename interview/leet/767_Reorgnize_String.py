#!/usr/bin/env python3

from collections import Counter
from heapq import heappush, heappop, heapify

class Solution:
    def reorganizeString(self, S):
        cnt, ret = Counter(S), ''
        for k in cnt:
            cnt[k] = -cnt[k]
        heap = [[v, k] for k, v in cnt.items()]
        heapify(heap)
        while heap:
            k1, c1 = heappop(heap)
            ret, k1 = ret+c1, k1+1
            if k1 < 0 and not heap:
                return ''
            if not heap:
                return ret
            k2, c2 = heappop(heap)
            ret, k2 = ret+c2, k2+1
            if k1 < 0:
                heappush(heap, [k1, c1])
            if k2 < 0:
                heappush(heap, [k2, c2])
        return ret

    # How to prove rigorously
    def reorganizeString_stefan(self, S):
        a = sorted(sorted(S), key=S.count)
        h = len(a) // 2
        print(a)
        a[1::2], a[::2] = a[:h], a[h:]
        print(a)
        print(a[-1:], a[-2:-1])
        return

S = 'aab'
S = 'aaabbbccc'
S = 'aaabc'
S = 'aaab'

sol = Solution()
print(sol.reorganizeString_stefan(S))
