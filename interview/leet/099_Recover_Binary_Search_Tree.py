#!/usr/bin/env python

import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        left, right = self.dualNode(root, None, None)
        left.val, right.val = right.val, left.val
        traverse(root)

    def isBST(self, node, minVal, maxVal):
        if node == None:
            print("Reach the None node: ", node)
            return (True, None, None, None)
        print('Processing Node: %s' % node.val)
        val = node.val
        if (maxVal != None and val > maxVal) or (minVal != None and val < minVal):
            print("Found the wrong one: %s" % node.val)
            flagC, wValC, minCondC, maxCondC = (False, val, minVal, maxVal)

        print("Going left for Node: %s" % node.val)
        flagL, wValL, minCondL, maxCondL = self.isBST(node.left, minVal, val)

        print("Going right for Node: %s" % node.val)
        flagR, wValR, minCondR, maxCondR = self.isBST(node.right, val, maxVal)

        print("Finished with node: %s" % node.val)

        if (not flagL) and (not flagR):
            print('Found exchange node in left and right branches: %d, %d' % (wValL, wValR))
            self.swapTwoNodes(node.left, wValR, wValL)
            self.swapTwoNodes(node.right, wValL, wValR)
            return (True, None, None, None)

        elif not flagL:
            if self.verifyCurrNodeWrongNode(val, minVal, maxVal, wValL, minCondL, maxCondL):
                print('Found exchange node: %s' % val)
                node.val = wValL
                self.swapTwoNodes(node.left, val, wValL)
                return (True, None, None, None)

            return (flagL, wValL, minCondL, minCondL)

        elif not flagR:
            if self.verifyCurrNodeWrongNode(val, minVal, maxVal, wValR, minCondR, maxCondR):
                print('Found exchange node: %s' % val)
                node.val = wValR
                self.swapTwoNodes(node.right, val, wValR)
                return (True, None, None, None)

            return (flagR, wValR, minCondR, minCondR)

        return (True, None, None, None)

    def swapTwoNodes(self, node, cVal, wVal):
        # print('I am in swapTwoNodes: node: %d, cVal %d, wVal %d' % (node.val, cVal, wVal))
        if node.val == wVal:
            node.val = cVal
        elif node.val < cVal:
            self.swapTwoNodes(node.right, cVal, wVal)
        else:
            self.swapTwoNodes(node.left, cVal, wVal)

    def verifyCurrNodeWrongNode(self, cVal, cMin, cMax, wVal, wMin, wMax):
        if cMin != None and wVal < cMin:
            return False
        if cMax != None and wVal > cMax:
            return False
        if wMin != None and cVal < wMin:
            return False
        if wMax != None and cVal > wMax:
            return False
        return True

    def headNode(self, node, minVal, maxVal):
        if node == None:
            return None
        val = node.val
        left = self.headNode(node.left, minVal, val)
        if left != None:
            return left
        right = self.headNode(node.right, val, maxVal)
        if (maxVal != None and val > maxVal) or (minVal != None and val < minVal):
            return val
        if right != None and node.val > right:
            return val
        return right

    def tailNode(self, node, minVal, maxVal):
        if node == None:
            return None
        val = node.val
        right = self.tailNode(node.right, val, maxVal)
        if right != None:
            return right
        left = self.tailNode(node.left, minVal, val)
        if (maxVal != None and val > maxVal) or (minVal != None and val < minVal):
            return val
        if left != None and node.val < left:
            return val
        return left

    def dualNode(self, node, minVal, maxVal):
        if node == None:
            return (None, None)
        val = node.val
        leftHead, leftTail = self.dualNode(node.left, minVal, val)
        rightHead, rightTail = self.dualNode(node.right, val, maxVal)
        if leftHead != None:
            left = leftHead
        elif (maxVal != None and val > maxVal) or (minVal != None and val < minVal):
            left = node
        elif rightHead!= None and node.val > rightHead.val:
            left = node
        else:
            left = rightHead

        if rightTail != None:
            right = rightTail
        elif (maxVal != None and val > maxVal) or (minVal != None and val < minVal):
            right = node
        elif leftTail != None and node.val < leftTail.val:
            right = node
        else:
            right = leftTail

        return (left, right)


def treeBuilder(nodeString):
    nodeList = nodeString[1:-1].split(',')
    nodeQueue = queue.Queue()
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
    print('Node: %d' % node.val)
    if node.left != None:
        print('Left: %d' % node.left.val)
    if node.right != None:
        print('Right: %d' % node.right.val)
    if node.left != None:
        traverse(node.left)
    if node.right != None:
        traverse(node.right)

sol = Solution()
nodeString = '[3,null,2,null,1]'
nodeString = '[2,3,1]'
nodeString = '[1,3,null,null,2]'
nodeString = '[3,1,4,null,null,2]'
root = treeBuilder(nodeString)
traverse(root)
print(sol.headNode(root, None, None))
print(sol.tailNode(root, None, None))
l, r = sol.dualNode(root, None, None)
print(l.val, r.val)
root = sol.recoverTree(root)
# traverse(root)
# wrong = sol.isBST(root, None, None)
# wrong = sol.isBST(None, None, None)
# print(wrong[1].val)
