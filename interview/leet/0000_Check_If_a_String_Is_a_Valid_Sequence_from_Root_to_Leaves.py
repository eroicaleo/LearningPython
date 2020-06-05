#!/usr/bin/env python3

from tree import *

class Solution:
    def isValidSequence(self, root, arr):
        l = len(arr)
        def dfs(root, ix):
            if root == None:
                return False
            if ix == l-1:
                return (root.val == arr[ix]) and (root.left == None) and (root.right == None)
            return (root.val == arr[ix]) and (dfs(root.left, ix+1) or dfs(root.right, ix+1))
        return dfs(root, 0)

root = '[8,3,null,2,1,5,4]'
arr = [8]
root = '[0,1,0,0,1,0,null,null,1,0,0]'
arr = [0,1,0,1]
root = '[0,1,0,0,1,0,null,null,1,0,0]'
arr = [0,0,1]
root = '[0,1,0,0,1,0,null,null,1,0,0]'
arr = [0,1,1]

node = treeBuilder(root)
traverse(node)
sol = Solution()
print(sol.isValidSequence(node, arr))
