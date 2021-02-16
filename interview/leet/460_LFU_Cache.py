#!/usr/bin/env python3

class ValNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return f'ValNode({self.val})'

class FreqNode:
    def __init__(self, cnt):
        self.next = self.prev = None
        self.cnt = cnt
        self.head = ValNode('^', '^')
        self.tail = ValNode('$', '$')
        self.stitch(self.head, self.tail)
        self.d = {}

    def __str__(self):
        ret = f'FreqNode({self.cnt}): '
        node = self.head
        while node:
            ret += f'ValNode({node.key},{node.val}), '
            node = node.next
        return '{'+ret+'}'

    def stitch(self, prev, next):
        prev.next = next
        next.prev = prev

    def remove(self, key):
        curr = self.d[key]
        prev, next = curr.prev, curr.next
        self.stitch(prev, next)
        del self.d[key]

    def insert(self, key, val):
        curr = ValNode(key, val)
        self.d[key] = curr
        self.stitch(curr, self.head.next)
        self.stitch(self.head, curr)

    def evict(self):
        key = self.tail.prev.key
        self.remove(key)
        return key

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = FreqNode(0)
        self.tail = FreqNode(float('inf'))
        self.stitch(self.head, self.tail)
        self.d = {}
        self.dv = {}

    def stitch(self, prev, next):
        prev.next = next
        next.prev = prev

    def get(self, key):
        if not key in self.d:
            return -1
        val = self.dv[key]
        self.touch(key, val)
        return val

    def put(self, key, value):
        if len(self.d) >= self.capacity:
            self.evict()
        self.dv[key] = value
        self.touch(key, value)

    def touch(self, key, val):
        # Get the curr FreqNode
        # Remove the ValNode from curr FreqNode
        if key in self.d:
            curr = self.d[key]
            curr.remove(key)
        else:
            curr = self.head

        # Get the next FreqNode, i.e. freq+1
        # If there is no such node, create one
        next = curr.next
        if curr.next.cnt != curr.cnt+1:
            prev, curr = curr, FreqNode(curr.cnt+1)
            self.stitch(prev, curr)
            self.stitch(curr, next)
        else:
            prev, curr = curr, next

        curr.insert(key, val)
        # remove prev if it's empty and it's not the head
        if len(prev.d) == 0 and prev.cnt > 0:
            self.stitch(prev.prev, curr)

        self.d[key] = curr

    def evict(self):
        first = self.head.next
        key = first.evict()
        if len(first.d) == 0:
            self.stitch(self.head, first.next)
        del self.d[key]
        del self.dv[key]

    def traverse(self):
        node_list = []
        node = self.head
        while node:
            node_list.append(str(node))
            node = node.next
        return '->'.join(node_list)

# cache = LFUCache(3)
# cmd_arg = [
# ('put', ('Shannon', 1)),
# ('get', ('Shannon',  )),
# ('put', ('Shannon', 2)),
# ('get', ('Shannon',  )),
# ('put', ('Wayne',   3)),
# ('get', ('Wayne',    )),
# ('get', ('Yang',     )),
# ('put', ('Yang',    1)),
# ('get', ('Yang',     )),
# ('put', ('Yukan',   1)),
# ]
# for cmd, arg in cmd_arg:
#     print(getattr(cache, cmd)(*arg))
#     print(cache.traverse())

cache = LFUCache(2)
cmd_arg = [
('put', (1, 1)),
('put', (2, 2)),
('get', (1,  )),
('put', (3, 3)),
('get', (2,  )),
('get', (3,  )),
('put', (4, 4)),
('get', (1,  )),
('get', (3,  )),
('get', (4,  )),
]
for cmd, arg in cmd_arg:
    print(getattr(cache, cmd)(*arg))
    # print(cache.traverse())
