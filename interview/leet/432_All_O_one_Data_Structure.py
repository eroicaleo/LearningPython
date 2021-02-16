#!/usr/bin/env python3

class Node:
    def __init__(self, cnt):
        self.next = self.prev = None
        self.cnt = cnt
        self.bucket = set()

    def __str__(self):
        return f'Node({self.cnt}, {self.bucket})'

class AllOne:
    def __init__(self):
        self.d = {}
        self.head = Node(0)
        self.tail = Node(float('inf'))
        self.stitch(self.head, self.tail)

    def stitch(self, prev, next):
        prev.next = next
        next.prev = prev

    def insert(self, curr, key):
        prev, next = curr.prev, curr.next
        curr.bucket.discard(key)
        if next.cnt == curr.cnt+1:
            prev, curr = curr, next
        else:
            prev, curr = curr, Node(curr.cnt+1)
            self.stitch(prev, curr)
            self.stitch(curr, next)
        curr.bucket.add(key)
        if len(prev.bucket) == 0 and prev.cnt > 0:
            self.stitch(prev.prev, curr)
        return curr

    def insert_before(self, curr, key):
        prev, next = curr.prev, curr.next
        curr.bucket.discard(key)
        if prev.cnt == curr.cnt-1:
            curr, next = prev, curr
        else:
            curr, next = Node(curr.cnt-1), curr
            self.stitch(prev, curr)
            self.stitch(curr, next)
        if curr.cnt > 0:
            curr.bucket.add(key)
        if len(next.bucket) == 0:
            self.stitch(curr, next.next)
        return curr

    def traverse(self):
        node_list = []
        node = self.head
        while node:
            node_list.append(str(node))
            node = node.next
        return '->'.join(node_list)

    def inc(self, key):
        self.d[key] = self.insert(self.d.get(key, self.head), key)

    def dec(self, key):
        if not key in self.d:
            return
        self.d[key] = self.insert_before(self.d[key], key)
        if self.d[key].cnt == 0:
            del self.d[key]

    def getMaxKey(self):
        return "" if len(self.d) == 0 else next(iter(self.tail.prev.bucket))

    def getMinKey(self):
        return "" if len(self.d) == 0 else next(iter(self.head.next.bucket))

sol = AllOne()
sol.inc(1)
print(sol.traverse())
print(sol.getMaxKey())
print(sol.getMinKey())
sol.inc(2)
print(sol.traverse())
sol.inc(1)
print(sol.traverse())
print(sol.getMaxKey())
print(sol.getMinKey())
sol.inc(2)
print(sol.traverse())
sol.inc(3)
print(sol.getMaxKey())
print(sol.getMinKey())
print(sol.traverse())
sol.dec(3)
print(sol.traverse())
sol.dec(3)
print(sol.traverse())
sol.dec(2)
print(sol.traverse())
sol.dec(1)
print(sol.traverse())
sol.dec(2)
print(sol.traverse())
sol.dec(1)
print(sol.traverse())
sol.dec(1)
print(sol.traverse())
