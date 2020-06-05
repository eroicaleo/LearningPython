
# The notes from CLRS

* The following snippet is the translation of Figure 22.3 in pg 595/616.
* When a vertex is not visited, it's color is white.
  when it's in queue, it's color is grey.
  when all it's neighbor has been visited, it's color is black.

```python
def bfs(G, s):
    l = len(G)
    color_list = ['white']*l
    d_list = [math.inf]*l
    parent_list = [None]*l

    color_list[s] = 'grey'
    d_list[s] = 0

    queue = collections.deque([s])
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if color_list[v] == 'white':
                color_list[v] = 'grey'
                d_list[v] = d_list[u]+1
                parent_list[v] = u
                queue.append(v)
        color_list[u] = 'black'
```

* One of the invariant of the `while` loop is all nodes in `queue` is grey.

# The notes from Princeton

* BFS (from source Vertex s)
    * Put s on to a FIFO queue, and mark s as visited. Repeat until the queue is empty.
    * Remove the least recently added vertex v
    * for each unmarked vertex pointing from v:
      add to queue and mark as visited.

```python
def bfs(self, G, sources):
    queue = deque(sources)
    for s in sources:
        self.marked[s] = 1
        self.distTo[s] = 0
    while queue:
        v = queue.popleft()
        for w in G.getAdj(v):
            if not self.marked[w]:
                self.marked[w] = 1
                self.edgeTo[w] = v
                self.distTo[w] = self.distTo[v]+1
                queue.append(w)
```

# The notes from leetcode problems

* typical BFS search uses a queue
* Sometimes the level is important, e.g. `329_Longest_Increasing_Path_in_a_Matrix.py`
  then we need to use 2 loops.

# For example: `129_Sum_Root_to_Leaf_Numbers.py`
```python
def sumNumbers2(self, root):
    if not root:
        return 0
    queue, res, node = collections.deque([(root, root.val)]), 0, root
    while queue:
        node, val = queue.popleft()
        if node.left:
            queue.append((node.left, 10*val+node.left.val))
        if node.right:
            queue.append((node.right, 10*val+node.right.val))
        if node.left == node.right == None:
            res += val
    return res
```

# For example: `417_Pacific_Atlantic_Water_Flow.py`

# For example: `329_Longest_Increasing_Path_in_a_Matrix.py`

* Convert the problem to a topological problem and use a BFS

* The `while` loop travels level by level
* The internal `for` loop traverse inside the level
  and when a node's indegree is 1'b, we add to `queue`

```python
while queue:
    for i in range(len(queue)):
        for w in graph.setdefault(queue.popleft(), []):
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
```
