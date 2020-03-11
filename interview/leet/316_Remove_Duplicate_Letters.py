#!/usr/bin/env python3

# Example 1:
# Input: "bcabc"Output: "abc"
# Example 2:
# Input: "cbacdcbc"
# Output: "acdb"

# My thinking process
# The first night, my first thought is to move a letter backward
# If the letter immediately after it is smaller than it, e.g.
# bab, we should move the 1st b back
# The difficulties we have, if we see
# dfadf, how do we know we need to drop 'df' at the beginning
# So I spend the whole day the next day, trying to figure out how to do this
#
# In the meantime, I am thing another way, I come up with a dict with locations
# in the list and see if I can find a sequence.
# a: [2, 13]
# b: [5]
# c: [0, 6, 9]
# d: [1, 10, 12]
# e: [3, 8]
# f: [4]
# k: [11]
# m: [7]
#
# Just before dinner, I came up with this idea, why don't try to move a letter forward
# as left as possible, this is the opposite to my first idea.
# Because if we have an 'a', we surely want to make it the first letter
# If there is a 'b' in front of 'a', that blocks 'a' moving forward, is because there is
# no 'b' after 'a'.
# So how we can know this information?
# My first thought is to use sth like my 2nd idea, but it turns out that a counter should
# be enough, when we see a letter 'c', we reduce counter[c] by 1, then at any position i,
# we will know how many 'c' left after position i.
# We will use a stack to implement this.
#
# Another thing that puzzles me a bit is, when we see letter 'c', and it's already in the stack 
# do we push it in stack? e.g., s = 'cdcdacd', when the stack is 'cd', do we push the second c?
# I think we can just skip it.

# Here is the example:
# s = 'cdaefbcmecdkda'
# stack =
# 'c'
# 'cd'
# pop c&d push a
# 'a'
# 'ae'
# 'aef'
# 'aefb'
# 'aefbc'
# 'aefbcm'
# 'aefbcme'
# 'c' already in stack, skip it, still 'aefbcme'
# 'aefbcmed'
# 'aefbcmedk'
# 'd' already in stack, skip it, still 'aefbcmedk'
# 'a' already in stack, skip it, still 'aefbcmedk'

import collections

class Solution:
    def removeDuplicateLetters(self, s):
        counter, stack = collections.Counter(s), ''
        for c in s:
            print(f'c = {c}')
            counter[c] -= 1
            if c in stack:
                continue
            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                stack = stack[:-1]
            stack += c
            print(f'stack = {stack}')
        return stack

s = 'cdaefbcmecdkda'
s = 'cbacdcbc'
s = 'bcabc'
# -> 'aefbcmdk'

print('d' < 'c')
sol = Solution()
print(sol.removeDuplicateLetters(s))

# a: [2]
# b: [0,3]
# c: [1,4]
# 
# a [2]
# b [1,6]
# c [0,3,5,7]
# d [4]
# 
# cfac
# a [2]
# c [0,3]
# f [1]
