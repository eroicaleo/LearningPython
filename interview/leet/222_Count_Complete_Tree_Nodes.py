#!/usr/bin/env python3

from tree import *

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        level, node = -1, root
        while node:
            node, level = node.left, level+1
        print(f'level = {level}')
        def traverse(n):
            h, node = level-1, root
            while node:
                print(f'traverse node = {node.val}, n={n}, h={h}')
                node, h, n = node.left if n < 2**h else node.right, h-1, n%(2**h)
            return h == -2
        lo, hi = 0, 2**level-1
        for i in range(2**level):
            print(f'i = {i}, {traverse(i)}')
        while (lo < hi):
            mi = lo+(hi-lo)//2
            print(f'mi = {mi}')
            if traverse(mi):
                lo = mi+1
            else:
                hi = mi-1
        print(f'final lo = {lo}')
        return (2**level-1)+(lo+1 if traverse(lo) else lo)
            

sol = Solution()
root = treeBuilder('[1,2,3,4]')
root = treeBuilder('[1,2,3]')
root = treeBuilder('[1,2,3]')
root = treeBuilder('[1,2]')
root = treeBuilder('[1,2,3,4,5,6,7]')
root = treeBuilder('[1]')
root = treeBuilder('[1,2,3,4,5,6]')
root = treeBuilder('[1,2,3,4,5]')
traverse(root)
print(sol.countNodes(root))
