#!/usr/bin/env python

import queue

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.loHeap = queue.PriorityQueue()
        self.hiHeap = queue.PriorityQueue()
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.hiHeap.put((num, num))
        print('I am pushing %d in hiHeap' % num)
        print('size of the two heaps: %d & %d' % (self.hiHeap.qsize(), self.loHeap.qsize()))
        tmp = self.hiHeap.get()[1]
        self.loHeap.put((-tmp, tmp))

        if self.hiHeap.qsize() < self.loHeap.qsize():
            tmp = self.loHeap.get()[1]
            self.hiHeap.put((tmp, tmp))

        print('size of the two heaps: %d & %d' % (self.hiHeap.qsize(), self.loHeap.qsize()))

    def findMedian(self):
        """
        :rtype: float
        """
        tmp = None
        if self.hiHeap.qsize() > self.loHeap.qsize():
            tmp = self.hiHeap.get()[1]
            self.hiHeap.put((tmp, tmp))
        elif self.hiHeap.qsize() > 0:
            tmpHi, tmpLo = self.hiHeap.get()[1], self.loHeap.get()[1]
            print('tmpHi and tmpLo: %d and %d' % (tmpHi, tmpLo))
            tmp = (tmpHi+tmpLo)/2
            self.hiHeap.put((tmpHi, tmpHi))
            self.loHeap.put((-tmpLo, tmpLo))
        return tmp

# loHeap = queue.PriorityQueue()
# loHeap.put((1, -1))
# loHeap.put((3, -3))
# print(loHeap.get())
sol = MedianFinder()
print(sol.findMedian())
sol.addNum(-1)
print(sol.findMedian())
sol.addNum(-2)
print(sol.findMedian())
sol.addNum(-3)
print(sol.findMedian())
sol.addNum(-4)
print(sol.findMedian())
sol.addNum(-5)
print(sol.findMedian())
# sol.addNum(-4)
# print(sol.findMedian())
# sol.addNum(-5)
# print(sol.findMedian())
