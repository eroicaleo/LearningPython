#!/usr/bin/env python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linkListBuilderFromList(l):
    if len(l) == 0:
        return None
    head = None
    for val in l[::-1]:
        prev, head = head, ListNode(val)
        head.next = prev
    return head

def linkListBuilder(nodeString):
    nodeList = nodeString[1:-1].split(',')
    print(nodeList)
    if len(nodeList) == 0 or nodeList[0] == '':
        return None
    head = ListNode(int(nodeList[0]))
    curr = head
    for val in nodeList[1:]:
        curr.next = ListNode(int(val))
        curr = curr.next
    return head

def traverse(head):
    curr = head
    while curr != None:
        print(curr.val, '->', sep='', end='')
        curr = curr.next
    print('None')
