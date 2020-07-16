#!/usr/bin/env python

# 508. Most Frequent Subtree Sum
# Medium
# 
# 617
# 
# 116
# 
# Add to List
# 
# Share
# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
# 
# Examples 1
# Input:
# 
#   5
#  /  \
# 2   -3
# return [2, -3, 4], since all the values happen only once, return all of them in any order.
# Examples 2
# Input:
# 
#   5
#  /  \
# 2   -5
# return [2], since 2 happens twice, however -5 only occur once.
# Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from tree import *

class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        self.d, self.m = {}, 0
        def post(root):
            if root == None:
                return 0
            s = post(root.left) + post(root.right) + root.val
            self.d.setdefault(s, 0)
            self.d[s] += 1
            if self.d[s] > self.m:
                self.m = self.d[s]
            return s
        post(root)
        return [k for k in self.d if self.d[k] == self.m]

nodeString = '[5,2,-3]'
nodeString = '[5,2,-5]'
root = treeBuilder(nodeString)
sol = Solution()
print(sol.findFrequentTreeSum(root))
