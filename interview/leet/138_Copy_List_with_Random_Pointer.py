#!/usr/bin/env python

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        while curr: 
            node = Node(curr.val, curr.next, None)
            curr.next, curr = node, curr.next
        curr = head
        while curr:
            copy = curr.next
            copy.random = curr.random.next
            curr.next = copy.next
        ret = copy = head.next
        while copy.next:
            copy = copy.next = copy.next.next
        return ret

