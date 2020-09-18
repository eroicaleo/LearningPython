#!/usr/bin/env python3

from collections import Counter

class Solution():
    def partitionLabels(self, S):
        cnt, s = Counter(S), set()
        i, ret = 0, []
        for c in S:
            i += 1
            s.add(c)
            cnt[c] -= 1
            if cnt[c] == 0:
                s.remove(c)
            if len(s) == 0:
                ret.append(i)
                i = 0
        return ret

    def partitionLabels_2(self, S):
        d = {c:i for i, c in enumerate(S)}
        hi, ret, j = 0, [], 0
        for i, c in enumerate(S):
            hi, j = max(hi, d[c]), j+1
            if hi == i:
                j, ret = 0, ret+[j]
        return ret

    def partitionLabels_2(self, S):
        d = {c:i for i, c in enumerate(S)}
        hi, ret, j = 0, [], -1
        for i, c in enumerate(S):
            hi = max(hi, d[c])
            if hi == i:
                j, ret = i, ret+[i-j]
        return ret


S = 'abcde'
S = 'ababcbacadefegdehijhklij'
sol = Solution() 
print(sol.partitionLabels(S))
print(sol.partitionLabels_2(S))
