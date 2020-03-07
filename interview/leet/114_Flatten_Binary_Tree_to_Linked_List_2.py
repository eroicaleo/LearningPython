#!/usr/bin/env python

from tree import *

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if root == None:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.prev
        self.prev = root
        return root
 
sol = Solution()
s = '[]'
s = '[1]'
s = '[1,2,5]'
s = '[1,2,5,3,4,null,6]'
s = '[1,2,5,3,4]'
root = treeBuilder(s)
traverse(root)
print('new tree')
traverse(sol.flatten(root))

