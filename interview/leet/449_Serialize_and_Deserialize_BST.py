#!/usr/bin/env python3

from tree import *
from collections import deque

class Codec:

    def serialize(self, root):
        self.ret = []
        def preorder(node):
            if node == None:
                return
            self.ret.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ' '.join(self.ret)

    def deserialize(self, data):
        data = deque(map(int, data.split()))
        def build(ub):
            if not data or data[0] > ub:
                return None
            node = TreeNode(data.popleft())
            node.left = build(node.val)
            node.right = build(ub)
            return node
        return build(float('inf'))

code = Codec()
nodestring = '[4,2,5,1,3]'
root = treeBuilder(nodestring)
traverse(code.deserialize(code.serialize(root)))
