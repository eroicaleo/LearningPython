#!/usr/bin/env python3

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while True:
            if (not fast) or (not fast.next):
                return -1
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        # # Get the loop length
        # l, fast = 1, fast.next
        # while slow != fast:
        #     l, fast = l+1, fast.next
        # Move the fast pointer by length l
        # slow = fast = head
        # for i in range(l):
        #     fast = fast.next
        i = 0
        while slow != fast:
            slow, fast, i = slow.next, fast.next, i+1
        return i
