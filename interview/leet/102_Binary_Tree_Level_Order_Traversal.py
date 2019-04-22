#!/usr/bin/env python

from tree import *

class Solution:
    def levelOrder(self, root):
        nodeList, valList, nextLevelList, ret = [root], [], [], []
        while len(nodeList) and nodeList[0]:
            for node in nodeList:
                valList.append(node.val)
                if node.left:
                    nextLevelList.append(node.left)
                if node.right:
                    nextLevelList.append(node.right)
            ret.append(valList)
            nodeList, nextLevelList, valList = nextLevelList, [], []
        return ret

nodeString = '[3,9,20,null,null,15,7]'
nodeString = ''
root = treeBuilder(nodeString)
traverse(root)
sol = Solution()
print(sol.levelOrder(root))
