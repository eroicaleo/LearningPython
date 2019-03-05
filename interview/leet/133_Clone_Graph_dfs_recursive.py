#!/usr/bin/env python

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dfs(currNode, visited):
            copyNode = Node(currNode.val, [])
            visited[currNode.val] = copyNode
            copyNode.neighbors = [visited[nextNode.val] if nextNode.val in visited else dfs(nextNode. visited) for nextNode in currNode.neighbors]
            return copyNode
        return dfs(node, {})

# for nextNode in currNode.neighbors
#     if nextNode.val not in visited:
#         dfs(nextNode, visited)
#     copyNode.neighbors.append(visited[nextNode.val])
