#!/usr/bin/env python3

from collections import Counter

class Solution:
    def minCostToMoveChips(self, position):
        cnt = Counter([p%2 for p in position])
        return min(cnt[0], cnt[1])

pos_list = [
[1,2,3],
[2,2,2,3,3],
[1,10000000000]
]

sol = Solution()
for position in pos_list:
    print(position, sol.minCostToMoveChips(position))
