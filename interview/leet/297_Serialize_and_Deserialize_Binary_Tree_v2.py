#!/usr/bin/env python

from tree import *

class Codec:

    def serialize(self, root):
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right) if root else 'n,'

    def deserialize(self, data):
        I = iter(data.split(','))
        def traverse():
            n = next(I)
            if n in ['', 'n']:
                return None
            node = TreeNode(int(n))
            node.left, node.right = traverse(), traverse()
            return node
        return traverse()
