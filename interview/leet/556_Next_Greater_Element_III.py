#!/usr/bin/env python

import bisect

class Solution:
    def nextGreaterElement(self, n):
        n, l = n//10, [n%10]
        while n:
            n, r = divmod(n, 10)
            if r < l[-1]:
                i = bisect.bisect_right(l, r)
                r, l[i] = l[i], r
                n = n*10+r
                for r in l:
                    n = n*10+r
                return n if n < 2**31 else -1
            l.append(r)
        return -1

n_list = [12354]
n_list = [1,12,21,12345, 53214, 111, 12354, 1999999999, 2147483647]
sol = Solution()
for n in n_list:
    print(n, sol.nextGreaterElement(n))
