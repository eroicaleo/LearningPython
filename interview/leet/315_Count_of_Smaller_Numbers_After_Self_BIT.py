#!/usr/bin/env python

class Solution:
    def countSmaller(self, nums):
        copy, length = sorted(list(nums)), len(nums)
        tree = [0]*(length+1)
        def index(val):
            l, r = 0, length-1
            while l < r:
                m = (l+r)//2
                if copy[m] < val:
                    l = m+1
                else:
                    r = m
            return l+1 # 1-based index
        def insert(i):
            while i <= length:
                tree[i] += 1
                i += (i&-i)
        def search(i):
            s = 0
            while i:
                s += tree[i]
                i -= (i&-i)
            return s
        ret = []
        for n in nums[::-1]:
            ix = index(n)
            ret.append(search(ix-1))
            insert(ix)
        return ret[::-1]

numsList = [
       [5,2,6,1],
       [52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41],
        ]
sol = Solution()

for nums in numsList:
    print(sol.countSmaller(nums))
