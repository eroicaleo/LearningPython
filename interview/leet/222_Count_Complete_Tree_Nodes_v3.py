#!/usr/bin/env python3

from tree import *

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l, r, h = root.left, root.left, 0
        while r:
            l, r, h = l.left, r.right, h+1
        if l: # right tree is fully grown
            return 2**h + self.countNodes(root.left)
        else: # left tree is fully grown
            return 2**h + self.countNodes(root.right)

    def countNodes2(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l, r, rr, h = root.left, root.left, root.right, 0
        while rr:
            l, r, rr, h = l.left, r.right, rr.right, h+1
        if not l: # whole tree from root is fully grown
            return 2**(h+1)-1
        if r: # left tree is fully grown
            return 2**(h+1) + self.countNodes(root.right)
        else: # right tree is fully grown
            return 2**h + self.countNodes(root.left)

sol = Solution()
# root = treeBuilder('[1,2,3,4,5,6]')
# root = treeBuilder('[1,2,3,4,5,6,7]')
# root = treeBuilder('[1,2,3,4,5]')
# root = treeBuilder('[1,2,3,4]')
# root = treeBuilder('[1,2,3]')
# root = treeBuilder('[1]')
# root = treeBuilder('[1,2]')
for i in range(1,8):
    root = treeBuilder(str(list(range(1, i+1))))
    traverse(root)
    print(sol.countNodes2(root))
