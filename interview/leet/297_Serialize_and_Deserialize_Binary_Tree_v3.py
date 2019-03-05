#!/usr/bin/env python

from tree import *

# Based on
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/234052/python-10-line-solution-beat-98

class Codec:

    def serialize(self, root):
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right) if root else 'n,'

    def deserialize(self, data):
        nodeList, self.index = data.split(','), 0
        def traverse():
            n, self.index = nodeList[self.index], self.index+1
            if (n in ['', 'n']) or self.index >= len(data):
                return None
            node = TreeNode(int(n))
            node.left, node.right = traverse(), traverse()
            return node
        return traverse()
