#!/usr/bin/env python3

from tree import *
import collections

class Solution:
    def sumNumbers(self, root):
        stack, node = [], root
        res = val = 0
        while node or stack:
            while node:
                val = 10*val + node.val
                node, stack = node.left, stack+[(node, val)]
                print(f'stack = {stack}')
            node, val = stack.pop(-1)
            if node.left == node.right == None:
                res += val
            node = node.right
        return res

    def sumNumbers2(self, root):
        if not root:
            return 0
        queue, res, node = collections.deque([(root, root.val)]), 0, root
        while queue:
            node, val = queue.popleft()
            if node.left:
                queue.append((node.left, 10*val+node.left.val))
            if node.right:
                queue.append((node.right, 10*val+node.right.val))
            if node.left == node.right == None:
                res += val
        return res

sol = Solution()
root = treeBuilder('[4,9,0,5,1]')
root = treeBuilder('[]')
root = treeBuilder('[0]')
root = treeBuilder('[1,2,3]')
traverse(root)
print(sol.sumNumbers2(root))
