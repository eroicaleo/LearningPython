#!/usr/bin/env python3

from tree import *

class Solution:
    def increasingBST(self, root):
        stack, node = [], root
        new_root = dummy = TreeNode(None)
        while stack or node:
            while node:
                stack, node = stack+[node], node.left
            node = stack.pop()
            print(f'poping node {node.val}')
            dummy.right = node
            node = node.right
            dummy = dummy.right
            dummy.left = dummy.right = None
        return new_root.right

node_string = '[2,1,3]'
node_string = '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
root = treeBuilder(node_string)
traverse(root)
sol = Solution()
print(f'After converting:')
traverse(sol.increasingBST(root))

