#!/usr/bin/env python

import queue

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = queue.PriorityQueue()
        di = dict()
        q.put((1, 1))
        di[1] = 1
        i = 0
        while (not q.empty()) and (i < n):
            d = q.get()[0]
            for j in [2, 3, 5]:
                dj = d * j
                if not d*j in di:
                    q.put((dj, dj))
                    di[dj] = dj
            i += 1
        return d

nList = range(1, 11)
sol = Solution()
for n in nList:
    print('#' * 80)
    print(sol.nthUglyNumber(n))
