#!/usr/bin/env python

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 1st travel, copy all the nodes
        visited, queue = dict(), set([node])
        while queue:
            currNode = queue.pop()
            if currNode.val in visited: continue
            copyNode = Node(currNode.val, [])
            visited[currNode.val] = copyNode
            for nextNode in currNode.neighbors:
                queue.add(nextNode)
        # 2nd travel
        visited2nd, queue, head = set(), set([node]), visited[node.val]
        while queue:
            currNode = queue.pop()
            if currNode.val in visited2nd: continue
            visited2nd.add(currNode.val)
            copyNode = visited[currNode.val]
            for nextNode in currNode.neighbors:
                queue.add(nextNode)
                copyNode.neighbors.append(visited[nextNode.val])
        return head
