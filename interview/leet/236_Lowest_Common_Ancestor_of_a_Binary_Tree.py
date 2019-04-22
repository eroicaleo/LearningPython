#!/usr/bin/env python

from tree import *

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return 0
        left  = self.lowestCommonAncestor(root.left,  p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        mid   = int(root.val in [p.val, q.val])
        if not left in [0, 1]:
            return left
        if not right in [0, 1]:
            return right
        if left+right+mid == 2:
            return root
        return left+right+mid

root, p, q = treeBuilder('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), TreeNode(1)
traverse(root)
sol = Solution()
print(sol.lowestCommonAncestor(root, p, q).val)
