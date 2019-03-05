#!/usr/bin/env python

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        head = Node(node.val, [])
        visited, queue = {node.val : head}, set([node])
        while queue:
            currNode = queue.pop()
            for nextNode in currNode.neighbors:
                if nextNode.val not in visited:
                    copyNode = Node(currNode.val, [])
                    visited[copyNode.val] = copyNode
                    queue.add(nextNode)
                else:
                    copyNode = visited[nextNode.val]
                visited[currNode.val].neighbors.append(copyNode)
        return head

