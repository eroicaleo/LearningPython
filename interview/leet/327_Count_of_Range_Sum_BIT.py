#!/usr/bin/env python

import itertools
import bisect

class Solution:
    def countRangeSum(self, nums, lower, upper):
        presum = list(itertools.accumulate(nums))
        copy, length = sorted(list(presum)), len(presum)
        tree = [0]*(1+length)
        print(f'presum = {presum}')
        print(f'copy = {copy}')
        def search(i):
            s = 0
            while i:
                s += tree[i]
                i -= (i&-i)
            return s
        def insert(i):
            while i <= length:
                tree[i] += 1
                i += (i&-i)
        ret = 0
        for n in presum:
            # l, r =  bisect.bisect_right(copy)
            r = bisect.bisect_right(copy, n-lower)
            l = bisect.bisect_left(copy, n-upper)
            m = 1+bisect.bisect_left(copy, n)
            print(f'n = {n}, r = {r}, n-lower = {n-lower}')
            print(f'n = {n}, l = {l}, n-upper = {n-upper}')
            print(f'n = {n}, m = {m}')
            inc = search(r)-search(l)+(lower<=n<=upper)
            ret += inc
            insert(m)
            print(f'inc = {inc}')
            print(f'after inserting {n}, index {m}, tree = {tree}')
        return ret



nums, lower, upper = [-2, 5, -1], -2, 2 #[0,0] [2,2] [0,2]
nums, lower, upper = [2147483647,-2147483648,-1,0], -1, 0

sol = Solution()
print(sol.countRangeSum(nums, lower, upper))
