* 314
* 1305 (done)
* 19 Remove Nth Node From End of List
* 273 and inverse function
* 708 
* 1498 (done) number of subsequence
* 543 (done) diameter of binary tree
* 560 (done) subarray sum equals K
* 938 (done) Range sum of BST

# High frequency

03/24
* 621 Task Scheduler (Done)
* 56 Merge Intervals (Done)
* 674 Longest Continuous Increasing Subsequence (Done)
* 10 Reg Exp Match (Done) Try again

03/25
* 0236 Lowest Common Ancestor Of A Binary Tree (Done)
* 0091 DecodeWays (Done)
* 0038 CountAndSay (Done)
* 0043 Multiply String (Done)
* 0173 Binary Search Tree Iterator (Done)
* 0151 Reverse Words in a String (Done)
* 0042 Trapping Rain Water (Done)

03/26
* 0449 SerDesBST (Done) left: iterative / Queue implementation
* 0339 Nested List Weight Sum (Done) left: BFS / iterative DFS
* 0029 Divide Two Integers (not Done)
* 0114 FlattenBinaryTreeToLinkedList (Done) left: iterative
* 1249 MinRemoveToMakeValidParentheses (Done)
* 1762 Buildings With an Ocean View (Done)

03/27

* 0921 Minimum Add to Make Parentheses Valid
    * Traverse through the string
* 0071 Simplify Path
    * Stack
* 0426 Convert Binary Search Tree to Sorted Doubly Linked List
    * in order traverse iterative
    * in order traverse recursive
    * Divide conqure by FLAGbigoffer is also pretty elegant: do the left side, then right side, connect root with left, the connect root with right.
* 0215 KthLargestElementInAnArray

03/28

* 1091ShortestPathInBinaryMatrix (Done)
    * remember to ask interviewer if we can change the original matrix

03/29

* CuttingRibbons1891 (Done)
    * Binary search, don't forget to set mi toward hi, otherwise will have infinite loop
      i.e. mi = (lo + hi + 1) / 2

* BasicCalculatorII0227 (Done)
    * Worth thinking again how to make the code cleaner.
    * The highest vote solution is really clear.

* FindPeakElement0162 (Done)
    * Binary search
        while (lo < hi) {
            int mi = (lo + hi) / 2;
            if (nums[mi] < nums[mi+1]) lo = mi + 1; // It must exist in [mi + 1, hi]
            else hi = mi; // It must exist in [lo, mi]
        }
        return lo;

* CapacityToShipPackagesWithinDDays1011
    * Binary search:
int d = getDays(weights, mi);
if (d > days) lo = mi + 1;
else hi = mi;

* IntervalListIntersections0986 (Done)
    * Similar to merge sort

03/30

* ProductOfTwoRunLengthEncodedArrays1868
    * This is like the combo of Merge Interveral and IntervalListIntersections0986
    * Used the implementation trick of Merge Interveral, to keep a reference to the last element.
* FindLargestValueInEachTreeRow0515
    * BFS
    * But can also use DFT by passing a level
* AddBoldTagInString0616
    * I use merge interval like solution
    * fast solution would be using String.indexOf to get all the chars that need to be bold
* AllNodesDistanceKInBinaryTree0863
    * traverse twice
    * But use a hash map is cleaner and worth to try.

03/31

* SwimInRisingWater0778
    * BFS + Priority Queue
* Word Break II
    * backtracking + memo
* VerticalOrderTraversalOfABinaryTree0987
    * DFS + Priority Queue
* MakeALargeIsland0827
    * DFS + component size
* AccountsMerge0721
    * Build a graph + DFS
    * Union and Find

04/01

* NextPermutation0031
    * Find the first in order pairs
* ContinuousSubarraySum0523
    * compute presum then use map and mod
* ValidNumber0065
    * My own statemachine implementation: very lengthy
    * Use 4 flags, boolean seenSign = false, seenDot = false, seenNum = false, seenE = false
      And check their relation is much cleaner
    * SM or DFA is more clearly in terms of thinking process.
* ValidWordAbbr0408
    * Use 2 pointers
* ExclusiveTimeOfFunctions0636
    * Stack
* CloneGraph0133
    * DFS clone

04/02

* DiagonalTraverse0498
    * The diagnol must satisfy n + m = K
    * For each K, determines the maxRow and minRow

```
int maxRow = Math.min(i, nr - 1);
int minRow = Math.max(i - nc + 1, 0);
```

04/03

* SearchInRotatedSortedArray0033
    * Always search for the monotoneous increasing half

```
        while (lo <= hi) {
            int mi = (lo + hi) / 2;
            if (nums[mi] == target) return mi;
            if (nums[mi] < nums[hi]) {
                if (target < nums[mi] || target > nums[hi]) hi = mi - 1;
                else lo = mi + 1;
            } else {
                if (target < nums[lo] || target > nums[mi]) lo = mi + 1;
                else hi = mi - 1;
            }
        }
        return -1;
```

04/04

* ValidPalindromeIII1216
    * Use 2-D dp table, `dp[i][j]` to record how many chars need to be deleted for s[i:j].
    * It can be done with only 1-D dp table
* Kth Missing Positive Number 1539
    * 一个萝卜一个坑
    * Convert the original array to missing array with this equation A[i] - i - 1
      then do the binary search to find the rightmost index < K

04/05

* RemoveAllAdjacentDuplicatesInString1047
    * Stack, use either the original array or a StringBuilder
* BinaryTreeVerticalOrderTraversal0314
    * BFS, use 2 queues, one for node, one for vertical level. 
    * No need to use treeMap, use minVerticalLevel and maxVerticalLevel to get all levels.
* DotProductOfTwoSparseVectors1570
    * Use two pointers, like merge sort
* LowestCommonAncestorOfABinaryTreeIII1650
    * Compute level first
    * Then align the level
    * Then move together
* InsertIntoSortedCircularLinkedList0708
    * 3 conditinos:
```
if (
                (slow.val <= val && val <= fast.val) ||
                (fast.val < slow.val && (fast.val > val || slow.val < val)) ||
                (fast == head)
            ) {
                ListNode node = new ListNode(val, fast);
                slow.next = node;
                break;
            }
```

* MaxConsecutiveOnesIII1004
    * I use dynamic programming, the dp table stores the starting point
    * Sliding window is clear

```
int l = 0, r;
for (r = 0; r < nums.length; r++) {
    if (nums[r] == 0) k--;
    if (k < 0 && nums[l] == 0) {
        l++;
        k++;
    }
}
return r - l;
```

* ConstructBinaryTreeFromString0536
    * typical recursive operation on the string
