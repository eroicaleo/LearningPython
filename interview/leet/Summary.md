# For prolems like return all trees or valid strings, e.g. 095 or 301
* There are general 2 ways: top down and bottom up
* top down is like eliminating invalid answers: 301
* bottom up is like constructing valid answers: 095

# Search:
* The key is to find a way to reduce problem size, either by half or linear
* Needs to find a clean way to implement, avoid using too many if ... else ...
* For example, 081 is by half
* e.g. 240 is by one row and one column
* e.g. 016 is converted to a problem like 240

# Counting:
* There are two ways to count, either by row or by column.
* Or count from start to current position, or from current position to end
  For example, problem 560, my solution is at position i, count to the end
  Better solution, from discussion form, at position i, count from the beginning

# Single number problem: general solution:
https://leetcode.com/problems/single-number-ii/discuss/43296/An-General-Way-to-Handle-All-this-sort-of-questions.
this kind of question the key idea is design a counter that record state. the problem can be every one occurs K times except one occurs M times. for this question, K =3 ,M = 1(or 2) .

# Heap problem:
* Use heapq is way much easier than queue.PriorityQueue. example: problem 295.
* however, with python 3 and `heapq`, you if you want to insert `(key, node)` into a
  `heapq`. And if `key` is the same for two tuples, then python don't know how to compare
  this tuple, so you have to do `(key1, key2, node)`, e.g. problem 23.
* The time complexity for heapify is O(N)

# Sorting problem:
In python, how to use custmized comparator.
example: problem 179.
how to use `key` in `sorted` function: problem 56.

# Depth first search
You always go one direction until stuck.
For example, if you travel a tree, then go left until left is Null, e.g. problem 145.
better example would be problem 98 v3.
And this is the example from leetcode: 
https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)
If you travel a graph, always go to the next node, e.g. problem 322.
Usually, the DFS can be achieved through recursion and iterative.
Another example is problem 133.

When using iterative approach, a stack will be used. And the code is Usually like the following,
with 2 while loop, when the inner while loop terminates, the stack is popped.
For iterative DFS for graph, it's quite similar to BFS. Consider problem 133, not done yet

```python
stack, node, prev = [], root, None
while node or stack:
    while node:
        stack, node = stack + [node], node.left
    node = stack.pop(-1)
    # do some processing about the current node
    node, prev = node.right, node
```

# Python tricks

* return something, but if something can be `None`, then can use `or`, problem 179
* For range in if statement, python can do `if 0 <= i < len(grid)`, problem 200
* To run a function on an iterables, can use `list(map(func, arg1, arg2, ...))`
  code is much more concise, but not necessarily faster. problem 200
* When we want to assign the same value to 2 variables, we can do: `dummy = currNode = ListNode(0)`
  e.g. problem 23.
* To concat list of list to a list, you can use `itertools.chain.from_iterable(your_list_of_lists)`
* sort a string, has to use ''.join(sorted(s)), problem 49
* 

# Array related problem

* Always consider if sorting can help, e.g. problem 016
* If index matters and if it needs to count freqeuncy, consider bucket sort, e.g. problem 220/347

# Tree problems

* Always consider if inorder/preorder/postorder can help, e.g. problem 098 v2/v3
* e.g. problem 297 v2/v3 use preorder to solve

# Some problems needs to prove some property

* E.g. 621 TaskScheduler.py, needs to prove use the most frequent characters to build frame can achieve the optimum
* e.g. 134 Gas station, needs to prove as long as the summation > 0, there must exist a path
* e.g. 310 Min height tree, needs to prove removing leaf nodes, the distances between the resting nodes stay the same

# Recursion

* A very typical example: problem 698

# Problems I feel hard to write code

* Problem 301 remove parentheses

# Problems I feel the solution is cool

* Problem 105 solution by

# Problems I cannot solve in the first round

* Problem 238/50

# Graph

* When we travel a graph, in some cases we need to mark some nodes visited.
  we can actually remove them with a "set" data structure, e.g. problem 127

# Similar problem

* skyline, heap
* water, two pointers
* 84 rectangle, stack

# parentheses problem:

* problem 301/22