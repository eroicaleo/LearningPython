#!/usr/bin/env python3

from tree import *

from collections import deque

class Solution:
    def largestValues(self, root): 
        if root == None:
            return []
        queue, ret = deque([root]), []
        while queue:
            m = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                m = max(node.val, m)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(m)
        return ret

root = treeBuilder('[1,3,2,5,3,null,9]')
traverse(root)
sol = Solution()
print(sol.largestValues(root))
