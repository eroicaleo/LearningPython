#!/usr/bin/env python

from tree import TreeNode

class BST:
    def __init__(self):
        self.root = None

    def put(self, val):
        self.root = self.put_int(self.root, val)

    def put_int(self, node, val):
        if node == None:
            return TreeNode(val)

        if val < node.val:
            node.left = self.put_int(node.left, val)
        elif val > node.val:
            node.right = self.put_int(node.right, val)
        else:
            node.self_count += 1
        node.size = node.self_count + self.size(node.left) + self.size(node.right)
        return node

    def size(self, node):
        if node == None:
            return 0
        else:
            return node.size

    def rank(self, val):
        return self.rank_int(self.root, val)

    def rank_int(self, node, val):
        if node == None:
            return 0

        if node.val > val:
            return self.rank_int(node.left, val)
        elif node.val == val:
            return self.size(node.left)
        else:
            return node.self_count + self.size(node.left) + self.rank_int(node.right, val)
