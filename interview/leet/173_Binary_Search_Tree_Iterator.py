#!/usr/bin/env python3

from tree import *

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        from collections import deque
        self.stack = deque()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop()
        ret, node = node.val, node.right
        while node:
            self.stack.append(node)
            node = node.left
        return ret

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0

treeString = '[7,3,15,null,null,9,20]'
root = treeBuilder(treeString)
traverse(root)
it = BSTIterator(root)
while it.hasNext():
    print(it.next())
