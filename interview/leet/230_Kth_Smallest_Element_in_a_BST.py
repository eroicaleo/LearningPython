#!/usr/bin/env python3

from tree import *

class Solution:
    def element(self, root, k):
        self.k, self.v = k, None
        def traverse(node):
            if not node:
                return False
            if traverse(node.left):
                return True
            self.k -= 1
            if self.k == 0:
                self.v = node.val
                return True
            return traverse(node.right)
        traverse(root)
        return self.v

    def element_iterative(self, root, k):
        stack, node = [], root
        while node or stack:
            while node:
                node, stack = node.left, stack + [node]
            node, k = stack.pop(-1), k-1
            if k == 0:
                return node.val
            node = node.right
        return None

sol = Solution()
root = treeBuilder('[5,2,7,0,3,6,8]')
root = treeBuilder('[1]')
traverse(root)
print(sol.element_iterative(root, 1))
print(sol.element_iterative(root, 6))
