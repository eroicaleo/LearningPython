#!/usr/bin/env python3

from tree import *
import itertools

class Solution:
    def allPossibleFBT(self, N):
        if N%2 == 0:
            return []
        def helper(n):
            if n == 1:
                return [TreeNode(0)]
            ret = []
            for i in range(1,n,2):
                for l, r in itertools.product(helper(i), helper(n-1-i)):
                    root = TreeNode(0)
                    root.left, root.right = l, r
                    ret.append(root)
            return ret
        return helper(N)

            
N = 3
N = 5
N = 7
sol = Solution()

print(list(map(treeToString, sol.allPossibleFBT(N))))
print(list(range(1,3,2)))
print(list(range(1,5,2)))
print(list(range(1,7,2)))
