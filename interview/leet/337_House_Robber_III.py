#!/usr/bin/env python3

from tree import *

class Solution:
    def rob(self, root: TreeNode) -> int:
        if root == None:
            return 0
        rob1 = self.rob(root.left) + self.rob(root.right)
        rob2 = 0
        if root.left:
            rob2 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            rob2 += self.rob(root.right.left) + self.rob(root.right.right)
        rob2 += root.val
        return max(rob1, rob2)

    def rob_new(self, root: TreeNode) -> int:
        def traverse(root):
            print(f'root = {root.val if root else None}')
            if root == None:
                return [0, 0]
            l, r = traverse(root.left), traverse(root.right)
            print(f'l={l}, r={r}')
            return [max(l[0]+r[0], l[1]+r[1]+root.val), l[0]+r[0]]
        return traverse(root)[0]


sol = Solution()
treestr = '[3,2,3,null,3,null,1]'
treestr = '[100]'
treestr = '[]'
treestr = '[100,101,null]'
treestr = '[100,1,2]'
treestr = '[3,4,5,1,3,null,1]'
root = treeBuilder(treestr)
print(sol.rob_new(root))
