
## Segment Tree implementation

* The segment tree with lazy propogation is implemented in `segment_tree.py`
* One example is `699_Falling_Squares.py`

### Iterative implementation

* Another iterative implementation is implemented in `segment_tree_v3.py`
    * The figure in [here](https://codeforces.com/blog/entry/18051) really helps me understand
      this iterative implementation.

* The iterative implementation build a tree of size `2n`, where `n` is the array size.
  node 1 to `n-1` is the internal node, node `n` to `2n-1` is leaf node, and is same as
  the array.

* We need to figure out what is modification, what is query
    * For example, `699_Falling_Squares.py` can be

### The confusion I have

* What does the push and pull means? 

`pull` method travels from the current node to root, e.g. 18 -> (18/2) = 9 -> (9/2) = 4 -> (4/2) = 2 -> (2/2) = 1
`push` method travels from the root to current, 1 -> 2 -> 4 -> 9 -> 18

* Why do we need pull at the end of update?

We can give a example that doesn't use pull

* Why in pull, we need to add `lazy[node]` to `tree[node]`

Let's say we update node 18 and 19 by 1, since they are covered by node 9, only node 9 has been touched
`tree[9] = 4, lazy[9] = 1`

Then when we are doing pull, the first step is to do `self.tree[9] = max(self.tree[18], self.tree[9])`
Since 18 and 19 hasn't been touched, `tree[9]` goes back to 3 again. But we have `lazy[9] = 1`, we add it back.
So we get the correct `tree[9]`.

```python
################################################################################
Original tree
################################################################################
================================================================================================================================
                                                           1: 15 (0)                                                           |
_______________________________________________________________________________________________________________________________|
                           2: 7 (0)                            |                           3: 15 (0)                           |
_______________________________________________________________|_______________________________________________________________|
           4: 3 (0)            |           5: 7 (0)            |           6: 11 (0)           |           7: 15 (0)           |
_______________________________|_______________________________|_______________________________|_______________________________|
   8: 1 (0)    |   9: 3 (0)    |   10: 5 (0)   |   11: 7 (0)   |   12: 9 (0)   |  13: 11 (0)   |  14: 13 (0)   |  15: 15 (0)   |
_______________|_______________|_______________|_______________|_______________|_______________|_______________|_______________|
 16: 0 | 17: 1 | 18: 2 | 19: 3 | 20: 4 | 21: 5 | 22: 6 | 23: 7 | 24: 8 | 25: 9 |26: 10 |27: 11 |28: 12 |29: 13 |30: 14 |31: 15 |
_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
################################################################################
update l = 2, r = 3, val = 1
################################################################################
apply node = 9, value = 1
update before pull(l0)
================================================================================================================================
                                                           1: 15 (0)                                                           |
_______________________________________________________________________________________________________________________________|
                           2: 7 (0)                            |                           3: 15 (0)                           |
_______________________________________________________________|_______________________________________________________________|
           4: 3 (0)            |           5: 7 (0)            |           6: 11 (0)           |           7: 15 (0)           |
_______________________________|_______________________________|_______________________________|_______________________________|
   8: 1 (0)    |   9: 4 (1)    |   10: 5 (0)   |   11: 7 (0)   |   12: 9 (0)   |  13: 11 (0)   |  14: 13 (0)   |  15: 15 (0)   |
_______________|_______________|_______________|_______________|_______________|_______________|_______________|_______________|
 16: 0 | 17: 1 | 18: 2 | 19: 3 | 20: 4 | 21: 5 | 22: 6 | 23: 7 | 24: 8 | 25: 9 |26: 10 |27: 11 |28: 12 |29: 13 |30: 14 |31: 15 |
_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
update after pull(l0) before pull(r0)
================================================================================================================================
                                                           1: 15 (0)                                                           |
_______________________________________________________________________________________________________________________________|
                           2: 7 (0)                            |                           3: 15 (0)                           |
_______________________________________________________________|_______________________________________________________________|
           4: 4 (0)            |           5: 7 (0)            |           6: 11 (0)           |           7: 15 (0)           |
_______________________________|_______________________________|_______________________________|_______________________________|
   8: 1 (0)    |   9: 4 (1)    |   10: 5 (0)   |   11: 7 (0)   |   12: 9 (0)   |  13: 11 (0)   |  14: 13 (0)   |  15: 15 (0)   |
_______________|_______________|_______________|_______________|_______________|_______________|_______________|_______________|
 16: 0 | 17: 1 | 18: 2 | 19: 3 | 20: 4 | 21: 5 | 22: 6 | 23: 7 | 24: 8 | 25: 9 |26: 10 |27: 11 |28: 12 |29: 13 |30: 14 |31: 15 |
_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
update after pull(r0)
================================================================================================================================
                                                           1: 15 (0)                                                           |
_______________________________________________________________________________________________________________________________|
                           2: 7 (0)                            |                           3: 15 (0)                           |
_______________________________________________________________|_______________________________________________________________|
           4: 4 (0)            |           5: 7 (0)            |           6: 11 (0)           |           7: 15 (0)           |
_______________________________|_______________________________|_______________________________|_______________________________|
   8: 1 (0)    |   9: 4 (1)    |   10: 5 (0)   |   11: 7 (0)   |   12: 9 (0)   |  13: 11 (0)   |  14: 13 (0)   |  15: 15 (0)   |
_______________|_______________|_______________|_______________|_______________|_______________|_______________|_______________|
 16: 0 | 17: 1 | 18: 2 | 19: 3 | 20: 4 | 21: 5 | 22: 6 | 23: 7 | 24: 8 | 25: 9 |26: 10 |27: 11 |28: 12 |29: 13 |30: 14 |31: 15 |
_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|
```

* After one `update`, what nodes are up-to-date, what nodes are out-of-date?

First, before `pull`, only the border nodes are touched/up-to-date.
For example, it we update [2,3], the border node are [9].
If we update [3, 10], the border node are [19, 5, 9, 26].

We need to prove 2 things:
1. only border nodes are touched.

Let's define border node and internal node.
Both border and internal's covered range fall inside [l, r].
A node is internal if the range which its parent covers also fall into [l, r], otherwise it's border node.

2. border nodes are up-to-date.

Then after calling `pull` method,
I think I can make the following proposition: after `update`, for a node whose descendents are border node,
then it's up-to-date.

Proof: Assume `n` is not a border node, but is the ancestor of a border node `bn`. Then according to definition,
the range `n` covers doesn't fall into [l, r], so it must cover either `l` or `r`. Then it will be visited during
`pull`.

Then we need to prove, `n` is up-to-date.

Note, the node visited during `pull` does not necessarily be up-to-date.
Consider [l,r]=[4,7], then 10/11 will be visited, but they are internal node, so they are out of date.

Consider, `lbn` is the left most border node, and it covers [l', r'], we want to show `l == l'`.
Assume `l < l'`, consider the border node `lbn'` covers `l`, then it's left to `lbn`, we have a contradiction.
Then we must have `l >= l'`, apparently, based on the definition of border node, we have `l <= l'`. So `l == l'`.

Same thing for `rbn`, which is the right most border node, it must corver `r`.

We go from `lbn` to its ancestor and also from `rbn` to its ancestor. At one node, they will merge.
before merge, the nodes on the path can only cover either `lbn` or `rbn`. Each of these nodes have 2 kids,
one kid cover either `lbn` or `rbn`, and its sibling is completely out of 
range or completely in the range.
When out of range, it hasn't been updated.
When in the range, it must be a border node, which is up-to-date.
In either case, this node will be up-to-date.

So my conclusion is: all border nodes and all nodes cover the left/right most border node are up-to-date.

* After multiple `update`, what is the status of each node? up-to-date? out-of-date? or else?

After multiple updates, for an node which covers [l, r], if there is an update [s, e] such that [l, r]
is an border node of [s, e] or l <= s or r >= e, then [l, r], should be "aware" of this update.

We define an update on range [s, e] is above an node [l, r], if [l, r] is an internal node of [s, e]

Then after multiple updates, [l, r] should be aware of all update [s, e] such that [l, r] intersects [s, e]
and [s, e] is not above [l, r].

* After multiple `update`, how can we guarantee the query is still valid?

* After `push` in `query`, what nodes are up-to-date, what nodes are out-of-date?

* Why do we need push at the start of update?

* How to prove this code guarantee to work? (Use simple increase for update and sum for query to analyze since it's easy)

* Different update and query functions

Some update is not order dependent, like increament. Some update is order dependent, like assignment.
Some query doesn't need to know the range, like max/min. Some query need to know the range, like, summation.
So assignment+summation is more complex than max+increament.
