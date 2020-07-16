#!/usr/bin/env python

from tree import *
from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        if root == None:
            return []
        queue, ret = deque([root]), []
        while queue:
            curr_level = []
            print(queue[0].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr_level.append(node.val)
            print(f'{curr_level} = curr_level')
            ret.append(curr_level)
        return ret[::-1]

nodestring = '[3,9,20,null,null,15,7]'
root = treeBuilder(nodestring)
sol = Solution()
traverse(root)
print(sol.levelOrderBottom(root))
