#!/usr/bin/env python3

# Example: Assume that the iterator is initialized to the beginning of the list: [1,2,3].
# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element.
# Calling next() after that still return 2.
# You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

# Below is the interface for Iterator, which is already defined for you.

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums, self.iter = nums, 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.iter < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        n, self.iter = self.nums[self.iter], self.iter+1
        return n

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator, self.p = iterator, None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.p == None:
            self.p = self.iterator.next()
        return self.p

    def next(self):
        """
        :rtype: int
        """
        n, self.p = self.peek(), None
        return n

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.p != None) or self.iterator.hasNext()

nums = [1,2,3]
iterator = Iterator(nums)
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())

# Your PeekingIterator object will be instantiated and called as such:
print('#'*80)
print('PeekingIterator')
print('#'*80)
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()
    print(f'iter.peek() = {iter.peek()}')
    print(f'iter.next() = {iter.next()}')

