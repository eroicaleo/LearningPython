* Minimum total container size
leet 1335 Min difficulty of a job schedule

* Five-Star Sellers
Heap and math. worth coding.

* Earliest Time To Complete Deliveries
The leetcode has better description.
Sort the open time ascending, sort the delivery time in reverse order.

* Count LRU Cache Misses
Use python `OrderedDict`
Done Python

* Nearest Cities
Create two hash tables. x-coordinates and y-coordinates.

* Choose a flask
Sort the requirements
Sort the each flask type
Use 2 pointers

* Throttling Gateway
In any minute, cannot exceed 3
In any given 10-min cannot exceed 20
In any given 60-min cannot exceed 60
Maintain 3 queues:
1-min window
10-min window
60-min window
worth coding.

* Slowest Key
Just iterate the list.

* Labeling System
Actually pretty much similar as "Longest String Without 3 Consecutive Characters"
worth coding.

* Unique Device Names
Hash table

* Turnstile
Build 2 queues

* Debt records
Hash table

* Baseball
Stack

* Find the highest profit
heap

* Items In Containers
iterate through string and only keep the bar location
Use the binary search to get the left bar and right bar

* Find the maximum available disk space
Leet code "sliding window maximum"
Use a deque, in the queue, store the index instead of value.
When we see an element, we compare the queue from the back, we could pop out the queue.

* Split String into Unique Primes
Backtracking + memorization, worth trying

* Fetch items to display
Regular sorting

* Count Teams/Review Combinations
Regular combination sum

* Highest Tenure
DFS

* Secret Fruit List
Just compare, worth coding

* Find related product
connected components DFS/BFS, worth coding
Done Python

* Zombie Matrix
Regular graph travel

* Top N Buzzwords
regular loop.

* Load Balancer
Partial sum from left,
partial sum from right,
worth coding
A similar question in leetcode is "Partition to K Equal Sum Subsets"
Done Python

* optimize memory usage
one hash table for foreground
one hash table for background
worth coding

* Find critical nodes
Cannot figure out
Search this title and can find in leetcode discussion
articulation points in a graph (geeksforgeeks)
worth coding

* Find Substrings
cannot figure out

* Partition string 
Same as leet 763 partition label

* Maximal Minimum Value Path II
Same as leet 1102 path with max min value.
Done python

* Longest String Made Up Of Only Vowels
Find the first and last non-vowel char, a, b.
Find the longest all-vowel substring in between, [c,d].
If remove just one substring, remove [a, b]. Return l-(b-a+1).
If remove 2 substrings. Return l-(b-a+1)+(d-c+1).
Worth coding.

* Subtree with Maximum Average
DFS. Same as Highest Tenure.

* Connect Ropes
Min-Heap.
Pop out 2 smallest and add them and push into heaps.

* Min Cost To Add New Roads
Union-Find. Worth coding.
Solution (Posted on the web):
Try to connect cities with minimum cost, then find small cost edge first, if two cities connected by the edge do no have same ancestor, then union them.
When number of unions equal to 1, all cities are connected.
Time Complexity: O(mlogm + mlogN). sort takes O(mlogm). find takes O(logN). With path compression and unino by weight, amatorize O(1).
Space: O(N).

* Min Cost to Repair Edges (Minimum Spanning Tree II)
Union-Find minimum spanning tree.
Worth coding.

* Data Center Critical Connection
Similar as “Find Cirtical Servers”. Worth coding.
Leetcode 1192 critical connections in a network 
Bridges in a graph in geeksforgeeks.
Done Python

* Movies on Flight
Sort and 2 pointers. One from beginning one from end.

* Treasure Island I
BFS seems better.

* Treasure Island II
BFS. worth coding.

* K Nearest Post Offices
Heap.

* Roll Dice
For 1 to 6, iterate the array, so 6N. Worth thinking twice.
Build a counter, go from 1 to 6.

* Min Cost to Connect All Nodes (Minimum Spanning Tree I)
Minimum spanning tree + Union/Find

* Cell State After N Days
Simple loop

* MOVE OBSTACLE
BFS. worth coding.

* SHOPKEEPER SALE
Iterate from right. Worth coding.

* Favorite Genres
Hash table. Worth coding JAVA.

* Longest String Without 3 Consecutive Characters

https://stackoverflow.com/questions/57740827/find-the-largest-string-such-that-a-b-c-are-not-continuos
Worth coding.
sort and characters, start from the most

