#!/usr/bin/env python

from linklist import *

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

class Solution:
    def rotateRight(self, head, k):
        if k == 0 or head == None or head.next == None:
            return head
        dummy = ListNode('dummy')
        dummy.next = head
        prev, l = dummy, 0
        while prev.next:
            prev, l = prev.next, l+1
        # print(f'The length is {l}')
        k = k%l
        if k == 0:
            return head
        prev = tail = dummy
        while k:
            prev, k = prev.next, k-1
        # print(f'after step 1 prev = {prev.val}')
        while prev.next:
            prev, tail = prev.next, tail.next
        # print(f'after step 2 prev = {prev.val}, tail = {tail.val}')
        head, tail.next, prev.next = tail.next, None, head
        return head


nodeString, k = '[]', 4
nodeString, k = '[1,2,3,4,5]', 2
nodeString, k = '[0,1,2]', 4
nodeString, k = '[0,1]', 4
nodeString, k = '[0]', 4
nodeString, k = '[1,2,3,4,5]', 0
head = linkListBuilder(nodeString)
traverse(head)
sol = Solution()
traverse(sol.rotateRight(head, k))
