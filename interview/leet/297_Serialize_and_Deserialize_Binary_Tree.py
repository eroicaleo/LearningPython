#!/usr/bin/env python

from tree import *

class Codec:

    def serialize(self, root):
        nodeQueue, i, data = [root], 0, ''
        while nodeQueue:
            node = nodeQueue.pop(0)
            data += 'n,' if not node else '%d,' % node.val
            if not node: continue
            nodeQueue.append(node.left)
            nodeQueue.append(node.right)
            i = len(data)
        return data[:max(0, i-1)]

    def deserialize(self, data):
        nodeQueue, i = [TreeNode(int(n)) if not n in ('n', '') else None for n in data.split(',')]+[None]*2, 1
        for node in nodeQueue:
            if not node: continue
            node.left, node.right, i = nodeQueue[i], nodeQueue[i+1], i+2
            if i > len(nodeQueue)-2: break
        return nodeQueue[0]

codec = Codec()
data = ''
data = '1,n,2'
data = '1'
data = '1,2'
data = '1,2,3,n,n,4,5'
print(codec.serialize(codec.deserialize(data)))
