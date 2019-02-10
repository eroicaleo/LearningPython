#!/usr/bin/env python

class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.val, self.key = val, key
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = dict()
        self.head, self.tail = None, None
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            if node == self.head:
                return node.val
            node.prev.next = node.next
            if node == self.tail:
                self.tail = node.prev
            else:
                node.next.prev = node.prev
            print('In get node: %d' % node.key)
            print('In get self.head: %d' % self.head.key)
            self.head.prev = node
            node.next, self.head, = self.head, node
            print('In get after swapping node: %d' % node.key)
            print('In get after swapping self.head: %d' % self.head.key)
            print('In get after swapping self.head.next.prev: %d' % self.head.next.prev.key)
            return node.val 
        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.get(key) != -1:
            self.head.val = value
        elif len(self.dict) < self.capacity:
            print("I am inserting new node: %d" % (key))
            node = self.Node(key, value)
            if len(self.dict) == 0:
                self.tail = node
            else:
                self.head.prev = node
            node.next, self.head = self.head, node
            print("new head: %d" % self.head.key)
            self.dict[key] = node
        else:
            self.get(self.tail.key)
            node = self.head
            node.val = value
            print('Prepare to delete key %d' % node.key)
            del self.dict[node.key]
            node.key = key
            self.dict[key] = node

cache = LRUCache(2)
print(cache.get(1))
cache.put(2, 6)
print(cache.get(1))
cache.put(1, 5)
cache.put(1, 2)
print(cache.get(1))
print(cache.get(2))

quit()
cache = LRUCache(2)
cache.put(1, 1)
print(cache.get(1))
print("now head: ", cache.head.key)
print(cache.get(2))
cache.put(2, 2)
print("now head: ", cache.head.key)
print(cache.get(1))
print("now head: ", cache.head.key)
print(cache.get(2))
cache.put(3, 3)
print(cache.get(2))
print(cache.get(1))
