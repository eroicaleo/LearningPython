#!/usr/bin/env python

import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        ret = []
        if root == None:
            return ret
        currNode = root
        stack = queue.LifoQueue()
        leftChecked = False
        i = 0
        while True:
            i += 1
            print("Iteration: %d, currNode: %s" % (i, currNode.val))
            if currNode.left != None and not leftChecked:
                stack.put(currNode)
                currNode = currNode.left
                leftChecked = False
                continue

            ret.append(currNode.val)
            print(ret)
            if currNode.right != None:
                currNode = currNode.right
                leftChecked = False
            elif not stack.empty():
                currNode = stack.get()
                leftChecked = True
            else:
                break

            if i > 100:
                break

        return ret

def treeBuilder(nodeString):
    nodeList = nodeString[1:-1].split(',')
    nodeQueue = queue.Queue()
    root = TreeNode(nodeList[0])
    currNode = root
    leftDone, rightDone = 0, 0
    for val in nodeList[1:]:
        print('processing %s' % val)
        print('leftDone,', leftDone, 'rightDone,', rightDone)
        if val != 'null':
            newNode = TreeNode(val)
            nodeQueue.put(newNode)
        else:
            newNode = None

        if leftDone == 0:
            currNode.left, leftDone = newNode, 1
        elif rightDone == 0:
            currNode.right, rightDone = newNode, 1
            leftDone, rightDone = 0, 0
            currNode = nodeQueue.get()
    return root

def traverse(node):
    print('Node: %s' % node.val)
    if node.left != None:
        print('Left: %s' % node.left.val)
    if node.right != None:
        print('Right: %s' % node.right.val)
    if node.left != None:
        traverse(node.left)
    if node.right != None:
        traverse(node.right)

sol = Solution()
nodeString = '[1,null,2,3,4,5,6,7,null,8,null,9]'
nodeString = '[-64,12,18,-4,-53,null,76,null,-51,null,null,-93,3,null,-31,47,null,3,53,-81,33,4,null,-51,-44,-60,11,null,null,null,null,78,null,-35,-64,26,-81,-31,27,60,74,null,null,8,-38,47,12,-24,null,-59,-49,-11,-51,67,null,null,null,null,null,null,null,-67,null,-37,-19,10,-55,72,null,null,null,-70,17,-4,null,null,null,null,null,null,null,3,80,44,-88,-91,null,48,-90,-30,null,null,90,-34,37,null,null,73,-38,-31,-85,-31,-96,null,null,-18,67,34,72,null,-17,-77,null,56,-65,-88,-53,null,null,null,-33,86,null,81,-42,null,null,98,-40,70,-26,24,null,null,null,null,92,72,-27,null,null,null,null,null,null,-67,null,null,null,null,null,null,null,-54,-66,-36,null,-72,null,null,43,null,null,null,-92,-1,-98,null,null,null,null,null,null,null,39,-84,null,null,null,null,null,null,null,null,null,null,null,null,null,-93,null,null,null,98]'
root = treeBuilder(nodeString)
traverse(root)
print(sol.inorderTraversal(root))
