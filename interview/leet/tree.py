#!/usr/bin/env python

import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.size = 1
        self.self_count = 1

def treeBuilder(nodeString):
    nodeList = nodeString[1:-1].split(',')
    nodeQueue = queue.Queue()
    if nodeList[0] == '':
        return None
    root = TreeNode(int(nodeList[0]))
    currNode = root
    leftDone, rightDone = 0, 0
    for val in nodeList[1:]:
        print('processing %s' % val)
        print('leftDone,', leftDone, 'rightDone,', rightDone)
        if val != 'null':
            newNode = TreeNode(int(val))
            print("create new node: %d" % newNode.val)
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
    if node == None:
        return
    print('Node: %d' % node.val)
    if node.left != None:
        print('Left: %d' % node.left.val)
    if node.right != None:
        print('Right: %d' % node.right.val)
    if node.left != None:
        traverse(node.left)
    if node.right != None:
        traverse(node.right)

def treeToString(root):
    nodeQueue = [root]
    currStr = ''
    # print(nodeQueue)
    while len(nodeQueue) > 0:
        node = nodeQueue[0]
        nodeQueue = nodeQueue[1:]
        # print(nodeQueue)
        if node == None:
            currStr += 'null,'
            # print(None)
        else:
            # print(node.val, node.left, node.right)
            nodeQueue += [node.left]
            nodeQueue += [node.right]
            currStr += str(node.val)+','
            # print(nodeQueue)
        # print(currStr)
    stringList = currStr[:-1].split(',')
    while stringList[-1] == 'null':
        stringList = stringList[:-1]
    currStr = ','.join(stringList)
    return currStr
