#!/usr/bin/env python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.numSmaller = 0
        self.numRepeat  = 1

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.root = None
        length = len(nums)
        ret = [0] * length
        i = length - 1
        while i >= 0:
            newNode = TreeNode(nums[i])
            self.root, size = self.insert(self.root, newNode)
            ret[i] = size
            i -= 1
        return ret

    def insert(self, node, newNode):
        if node == None:
            # print('Finish node %d, numSmaller: %d, numRepeat: %d' % (newNode.val, newNode.numSmaller, newNode.numRepeat))
            return (newNode, newNode.numSmaller)

        if node.val == newNode.val:
            node.numRepeat += 1
            size = node.numSmaller
        elif node.val > newNode.val:
            node.numSmaller += 1
            node.left, size = self.insert(node.left, newNode)
        elif node.val < newNode.val:
            node.right, size = self.insert(node.right, newNode)
            size += (node.numSmaller + node.numRepeat)
        # print('Finish node %d, numSmaller: %d, numRepeat: %d, size: %d' % (node.val, node.numSmaller, node.numRepeat, size))
        return node, size

numsList = [
       [5,2,6,1],
       [52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41],
        ]
sol = Solution()

for nums in numsList:
    print(sol.countSmaller(nums))
