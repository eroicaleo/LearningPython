#!/usr/bin/env python

from tree import *

class Solution:
    def flatten(self, root):
        def helper(root):
            if root == None:
                return None, None

            l_head, l_tail = helper(root.left)
            r_head, r_tail = helper(root.right)
            root.right = l_head or r_head
            root.left = None
            if l_tail:
                l_tail.right = r_head
            tail = r_tail or l_tail or root

            # print(f'root: {root.val}, tail: {tail.val}')
            return root, tail
        return helper(root)[0]

sol = Solution()
s = '[]'
s = '[1]'
s = '[1,2,5]'
s = '[1,2,5,3,4]'
s = '[1,2,5,3,4,null,6]'
root = treeBuilder(s)
traverse(root)
print('new tree')
traverse(sol.flatten(root))

