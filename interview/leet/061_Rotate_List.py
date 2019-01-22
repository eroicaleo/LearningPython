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
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return None 
        while True:
            first, second, n = head, head, 1
            while first.next != None and n <= k:
                first, n = first.next, n+1
            if (k == 0) or (n == k and first.next == None):
                return head
            elif k < n:
                break
            k = k % n
            print(k, n)
        while first.next != None:
            first, second = first.next, second.next
        first.next, second.next, head = head, None, second.next
        return head

nodeString, k = '[1,2,3,4,5]', 0
nodeString, k = '[0,1,2]', 4
nodeString, k = '[0,1]', 4
nodeString, k = '[0]', 4
nodeString, k = '[]', 4
head = linkListBuilder(nodeString)
traverse(head)
sol = Solution()
traverse(sol.rotateRight(head, k))
