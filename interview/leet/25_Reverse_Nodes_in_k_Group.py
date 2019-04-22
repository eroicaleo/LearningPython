#!/usr/bin/env python

from linklist import *

class Solution:
    def reverseKGroup(self, head, k):
        new_head = None
        while True:
            i, tail = 1, head
            while i < k and tail != None:
                tail, i = tail.next, i+1
            if i < k-1:
                break
            next_head = tail.next
            print(head.val, tail.val, next_head.val if next_head else next_head)
            while head != tail:
                prev_head = head
                head = head.next
                prev_head.next = tail.next
                tail.next = prev_head
            if new_head == None:
                new_head = tail
            head = next_head
            traverse(new_head)
        return head

sol = Solution()
head = linkListBuilderFromList([1,2,3,4,5])
traverse(head)
traverse(sol.reverseKGroup(head, 2))
