#!/usr/bin/env python3

from tree import *
import collections

class Solution:
    def sumNumbers(self, root):
        val, ret = 0, 0
        stack, node = [], root
        while node or stack:
            while node:
                val = 10*val+node.val
                stack, node = stack+[(node, val)], node.left
            node, val = stack.pop()
            if node.left == node.right == None:
                ret += val
            node = node.right
        return ret

    def sumNumbers3(self, root):
        self.res = 0
        def helper(root, s):
            if not root:
                return
            val = 10*s+root.val
            helper(root.left, val)
            helper(root.right, val)
            if root.left == root.right == None:
                self.res += val
        helper(root, 0)
        return self.res

sol = Solution()
root = treeBuilder('[0]')
root = treeBuilder('[]')
root = treeBuilder('[4,9,0,5,1]')
root = treeBuilder('[1,2,3]')
traverse(root)
print(sol.sumNumbers3(root))
