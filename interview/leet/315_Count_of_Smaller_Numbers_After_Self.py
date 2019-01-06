#!/usr/bin/env python

from BST import BST
from tree import *

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tree = BST()
        nums.reverse()
        ret = []
        for n in nums:
            tree.put(n)
            ret = [tree.rank(n)] + ret
            print(ret)
        # traverse(tree.root)
        return ret
# [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
#        [52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41],
numsList = [
       [5,2,6,1],
        ]
sol = Solution()

for nums in numsList:
    sol.countSmaller(nums)

