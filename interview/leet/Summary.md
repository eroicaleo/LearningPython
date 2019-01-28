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

# Single number problem: general solution:
https://leetcode.com/problems/single-number-ii/discuss/43296/An-General-Way-to-Handle-All-this-sort-of-questions.
this kind of question the key idea is design a counter that record state. the problem can be every one occurs K times except one occurs M times. for this question, K =3 ,M = 1(or 2) .

# Heap problem:
Use heapq is way much easier than queue.PriorityQueue
example: problem 295.

# Sorting problem:
In python, how to use custmized comparator.
example: problem 179.

# Depth first search
You always go one direction until stuck.
For example, if you travel a tree, then go left until left is Null, e.g. problem 145.
If you travel a graph, always go to the next node, e.g. problem 322.
Usually, the DFS can be achieved through recursion and iterative.
When using iterative approach, a stack will be used. And the code is Usually like the following,
with 2 while loop, when the inner while loop terminates, the stack is popped.

```python
stack = [root]
while stack: # Note here, we don't need to do len(stack)
    while node:
        stack += [node]
	node = node.left
```
