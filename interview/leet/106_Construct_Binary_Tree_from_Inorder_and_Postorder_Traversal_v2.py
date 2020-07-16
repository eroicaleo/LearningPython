#!/usr/bin/env python

from tree import *

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        l, prev, stack = len(inorder), None, []
        in_ix = po_ix = 0
        while in_ix < l or po_ix < l:
            if stack and stack[-1].val == postorder[po_ix]:
                curr = stack.pop()
                curr.right = prev
                po_ix += 1
                prev = curr
            else:
                curr = TreeNode(inorder[in_ix])
                curr.left = prev
                if inorder[in_ix] == postorder[po_ix]:
                    prev = curr
                    in_ix += 1
                    po_ix += 1
                else:
                    stack.append(curr)
                    in_ix += 1
                    prev = None
        return prev


sol = Solution()
inorder  = [9,3,15,20,7]
postorder = [9,15,7,20,3]
inorder  = [7,20,3]
postorder = [7,20,3]
inorder  = [3,20,7]
postorder = [7,20,3]
inorder  = []
postorder = []
inorder  = [2,3,1]
postorder = [3,2,1]
root = sol.buildTree(inorder, postorder)
traverse(root)
