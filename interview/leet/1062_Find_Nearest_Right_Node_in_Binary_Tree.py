#!/usr/bin/env python

from tree import *
from collections import deque

class Solution:
    def findNearestRightNode(self, root, u):
        queue = deque([root])
        found = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if found:
                    return node
                elif node.val == u.val:
                    found = True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if found:
                return None
        return None

nodeString = '[3,null,4,2]'
root = treeBuilder(nodeString)
u = root.right.left
nodeString = '[1,2,3,null,4,5,6]'
root = treeBuilder(nodeString)
u = root.left.right
nodeString = '[3,4,2,null,null,null,1]'
root = treeBuilder(nodeString)
u = root.left

print(f'u: {u.val}')
sol = Solution()
node = sol.findNearestRightNode(root, u)
print(f'node: {node if node == None else node.val}')
