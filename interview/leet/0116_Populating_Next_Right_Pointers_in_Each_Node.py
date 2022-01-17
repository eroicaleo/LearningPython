#!/usr/bin/env python3

class Solution:
    def connect(self, root):
        curr_head = root
        while curr_head:
            next_head, head = curr_head.left, curr_head
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            curr_head = next_head

    def connect_stefan(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
