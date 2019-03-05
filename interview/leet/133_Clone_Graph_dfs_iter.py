#!/usr/bin/env python

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        stack, visited, currNode = [], {}, node
        while stack or currNode:
            while currNode:
                if currNode.val not in visited:
                    copyNode = Node(currNode.val, [])
                    stack = stack + [currNode]
                currNode = currNode.neighbors.pop(0)
