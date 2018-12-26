#!/usr/bin/env python

from tree import *

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        currLevel = queue.LifoQueue()
        nextLevel = queue.LifoQueue()
        reverse = False
        if root == None:
            return []
        currLevel.put(root)
        ret = []
        while True:
            reverse = (not reverse)
            currList = []
            # print(reverse)
            while not currLevel.empty():
                node = currLevel.get()
                currList.append(node.val)
                # print(node.val)
                if reverse:
                    if node.left != None: nextLevel.put(node.left) 
                    if node.right != None: nextLevel.put(node.right) 
                else:
                    if node.right != None: nextLevel.put(node.right) 
                    if node.left != None: nextLevel.put(node.left) 
            ret.append(currList)
            currLevel, nextLevel = nextLevel, currLevel
            if currLevel.empty():
                break
        return ret

sol = Solution()
nodeStringList = [
        '[3,9,20,null,null,15,7]',
        '[]'
]
for nodeString in nodeStringList:
    root = treeBuilder(nodeString)
    traverse(root)
    print(sol.zigzagLevelOrder(root))
