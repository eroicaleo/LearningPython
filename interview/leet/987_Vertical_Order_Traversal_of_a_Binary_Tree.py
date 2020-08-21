#!/usr/bin/env python3

from tree import *
from collections import deque

class Solution:
    def verticalTraversal(self, root): 
        queue, y, d = deque([[root, 0]]), 0, {}
        while queue:
            for _ in range(len(queue)):
                node, x = queue.popleft()
                d.setdefault(x, []).append([y, node.val])
                if node.left:
                    queue.append([node.left, x-1])
                if node.right:
                    queue.append([node.right, x+1])
            y += 1
        return [[v for y, v in sorted(d[k])] for k in sorted(d)]


root = treeBuilder('[3,9,20,null,null,15,7]')
root = treeBuilder('[1,2,3,4,5,6,7]')
traverse(root)
sol = Solution()
print(sol.verticalTraversal(root))
