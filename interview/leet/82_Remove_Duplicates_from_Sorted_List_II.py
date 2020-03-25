#!/usr/bin/env python

from linklist import *

class Solution:
    def deleteDuplicates_iter(self, head):
        dummy = ListNode(None)
        back, dummy.next = dummy, head
        while True:
            print(f'back = {back.val}, head = {head.val if head else None}')
            while head and head.next and (back.next.val == head.next.val):
                back.next = head = head.next
            print(f'back.next.val = {back.next.val}, head.next.val = {head.next.val}')
            if not head:
                break
            else:
                back, head = back.next, head.next
        return dummy.next

    def deleteDuplicates(self, head):
        print(f'head = {head.val if head else None}')
        if head == None:
            return None
        flag = 0
        while head and head.next and (head.val == head.next.val):
            flag = 1
            head = head.next
        if flag:
            head = head.next
        print(f'before recursive')
        traverse(head)
        head.next = self.deleteDuplicates(head.next)
        print(f'after recursive')
        traverse(head)
        return head
        # print(f'head.val = {head.val}, head.next.val = {head.next.val}')


node_str = '[1,1,1,2,3]'
node_str = '[1,2,3,3,4,4,5]'
head = linkListBuilder(node_str)
traverse(head)
sol = Solution()
traverse(sol.deleteDuplicates(head))
