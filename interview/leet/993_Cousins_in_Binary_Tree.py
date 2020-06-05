#!/usr/bin/env python3

from tree import *

class Solution:
    def isCousins(self, root, x, y):
        queue = [(root, None)]
        while queue:
            next_queue, parents = [], []
            for q in queue:
                if q[0] == None:
                    continue
                p = q[0].val
                next_queue += [(q[0].left, p), (q[0].right, p)]
                if p in [x, y]:
                    parents.append(q[1])
            if len(parents) == 2 and (parents[0] != parents[1]):
                return True
            elif len(parents) > 0:
                return False
            queue = next_queue
        return False

nodeString = '[1,2,3,null,4,null,5]'
x = 5
y = 4
nodeString = '[1,2,3,4]'
x = 4
y = 3
nodeString = '[1,2,3,null,4]'
x = 2
y = 3
root = treeBuilder(nodeString)
traverse(root)
sol = Solution()
print(sol.isCousins(root, x, y))
