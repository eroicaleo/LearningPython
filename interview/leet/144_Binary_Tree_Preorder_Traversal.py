#!/usr/bin/env python

from tree import *

import queue

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = queue.LifoQueue()
        stack.put(root)
        ret = []
        while not stack.empty():
            node = stack.get()
            if node.right:
                stack.put(node.right)
            if node.left:
                stack.put(node.left)
            ret.append(node.val)
        return ret

sol = Solution()
nodeStringList = [
        '[1,null,2,3]',
        '[]'
]
for nodeString in nodeStringList:
    root = treeBuilder(nodeString)
    traverse(root)
    print(sol.preorderTraversal(root))
