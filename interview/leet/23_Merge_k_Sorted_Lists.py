#!/usr/bin/env python

from linklist import *
from heapq import heapify, heapreplace, heappop

class Solution:
    def mergeKLists(self, lists):
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapify(heap)
        dummy = currNode = ListNode(0)
        while heap:
            v, i, n = heap[0]
            currNode.next = heapreplace(heap, (n.next.val, i, n.next))[-1] if n.next else heappop(heap)[-1]
            currNode = currNode.next
        return dummy.next

listString = [
        '"1,4,5"',
        '"1,3,4"',
        '"2,6"',
        ]
listString = [
        '""',
        ]
lists = [linkListBuilder(s) for s in listString]
for l in lists:
    traverse(l)

sol = Solution()
traverse(sol.mergeKLists(lists))
