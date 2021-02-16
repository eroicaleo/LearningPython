#!/usr/bin/env python3

from tree import *
from collections import deque

class Codec:

    def serialize(self, root):
        return '' if not root else ' '.join([str(root.val), self.serialize(root.left), self.serialize(root.right)]).rstrip()

    def deserialize(self, data):
        data = list(map(int, data.split()))
        l, self.i = len(data), 0
        def build(ub):
            if self.i >= l or data[self.i] > ub:
                return None
            node, self.i = TreeNode(data[self.i]), self.i+1
            node.left = build(node.val)
            node.right = build(ub)
            return node
        return build(float('inf'))

code = Codec()
nodestring = '[4,2,5,1,3]'
root = treeBuilder(nodestring)
print(code.serialize(root))
traverse(code.deserialize(code.serialize(root)))

