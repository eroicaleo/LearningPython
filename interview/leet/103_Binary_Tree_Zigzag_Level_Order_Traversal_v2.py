#!/usr/bin/env python

from tree import *
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        queue, flip, ret = deque([root]), 0, []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flip:
                level.reverse()
            ret, flip = ret + [level], 1-flip
        return ret

sol = Solution()
nodeStringList = [
        '[3,9,20,null,null,15,7]',
        '[]'
]
for nodeString in nodeStringList:
    root = treeBuilder(nodeString)
    traverse(root)
    print(sol.zigzagLevelOrder(root))
