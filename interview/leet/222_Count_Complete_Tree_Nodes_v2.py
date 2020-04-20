#!/usr/bin/env python3

from tree import *

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        lh = rh = 0
        l = r = root

        while l:
            l, lh = l.left, lh+1
        while r:
            r, rh = r.right, rh+1

        print(f'lh = {lh}, rh = {rh}')
        if rh == lh:
            return (1<<rh)-1;
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

    def countNodes2(self, root: TreeNode) -> int:
        def helper(root, lh, rh):
            if root == None:
                return 0
            l = r = root
            if lh == None:
                lh = 0
                while l:
                    l, lh = l.left, lh+1
            if rh == None:
                rh = 0
                while r:
                    r, rh = r.right, rh+1

            print(f'lh = {lh}, rh = {rh}')
            if rh == lh:
                return (1<<rh)-1;
            return 1+helper(root.left, lh-1, None)+helper(root.right, None, rh-1)
        return helper(root, None, None)

    def countNodes_iterative(self, root: TreeNode) -> int:
        def height(node):
            h = -1
            while node:
                node, h = node.left, h+1
            return h
        nodes, h = 0, height(root)
        while root:
            if height(root.right) == h-1:
                nodes += (1<<h)
                root = root.right
            else:
                nodes += (1<<(h-1))
                root = root.left
            h -= 1
        return nodes

sol = Solution()
root = treeBuilder('[1,2,3,4]')
root = treeBuilder('[1,2,3]')
root = treeBuilder('[1,2,3]')
root = treeBuilder('[1,2]')
root = treeBuilder('[1,2,3,4,5,6,7]')
root = treeBuilder('[1,2,3,4,5,6]')
root = treeBuilder('[1]')
root = treeBuilder('[1,2,3,4,5]')
traverse(root)
print(sol.countNodes_iterative(root))

