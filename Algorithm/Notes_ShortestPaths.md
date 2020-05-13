
## 15.B Shortest-Paths Property

* Shortest Paths tree (SPT) exists
* `distTo[v]` is the length from `s` to `v`
* `edgeTo[v]` is the last edge on Shortest paths from `s` to `v`

### Edge relaxation

* `distTo[v]` is length of shortest known path from `s` to `v`
* `distTo[w]` is length of shortest known path from `s` to `w`
* `edgeTo[w]` is the last edge on the shortest known path from `s` to `w`
* if `v->w` gives shorter path to w through, updated both `edgeTo[w]` and `distTo[w]`.

### Optimality conditions

* `distTo[v]` are the shortest paths distances from s `<=>`
    * `distTo[s] = 0`
    * `distTo[v]` is the length of some path from s to v
    * For each edge `e=v->w`, `distTo[w] <= distTo[v] + e.weight()`

### Generic algorithm

* Relax any edge, repeat until optimality conditions are satisfied. 

## 15.C Dijkstra's Algorithm

### correctness

* `distTo[v]` will not change after `v` is relaxed
    * This is not obvious to me
* I think it's better to use induction:
    * `n = 1`, `v1` is the shortest, obvious
    * `n = k+1`, `v1, ..., vk` all have the shortest path and they
      are the first k closest vertices from `s`
    * Assume `v(k+1)` is the next vertex popped from heap.
    * Assume the `s ... w -> v(k+1)` is the shortest path, then `s -> w`
      must be in the first k closes vertices from `s`

### Spanning trees

* Similarity: both Dijkstra and Prim are in a family of algorithms that compute a graph's
  spanning tree.
* Distinction:
    * Prim's: Closest vertex to the tree (via an undirected edge)
    * Dijkstra's: Closest vertex to the source (via a directed path)
    * Both DFS and BFS are also in the same family.

### Complexity

* V insert, V delete-min, E decrease-key
* binary heap
    * insert: `logV`
    * delete-min: `logV`
    * decrease-key: `logV`
    * total: `E logV`

## 15.D Edge-Weighted DAGs

### Acyclic edge-weighted digraphs

* For no directed cycles, is it easier to find shortest paths than in a general digraph?
    * Yes
    * Sort the vertex in topological order

### Shortest paths in edge-weighted DAGs

* Topological sort algorithm computes SPT in any edge weighted DAG in time proportional to `E+V`
    * weight can even be negative
* Proof:
    * Each edge is relaxed exactly once, when v is relaxed,
      leaving `distTo[w] <= distTo[v] + e.weight()`
    * Inequality holds until algorithm terminates because:
        1. `distTo[w]` cannot increase
        2. `distTo[v]` will not change since it's topological order
    * Shortest path optimality conditions hold
