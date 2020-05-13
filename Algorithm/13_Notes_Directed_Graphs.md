
# 13.A Introduction

## Some digraph problems

* Path: is there a directed path from s to t?
* Shortest path: what is the shortest directed path from s to t?
* Topo sort: can you draw a digraph so that all edges point upwards?
* Strong connectivity: Is there a directed path between all pairs of vertices?
* Transitive closure: For which vertices v and w is there a path from v to w?
* PageRank: What is the importance of a web page?

# 13.B Digraph API

# 13.C Digraph Search 

## Reachability

## DFS in digraphs

## Reachability application: program control-flow analysis

* Every program is a digraph
    * Vertex = basic block of instrctions (straight-line program)
    * Edge = jump
* Dead-code elimination
    * Find and remove unreachable code.
* infinite-loop detection
    * Determine whether exit is unreachable.

## Reachability application: mark sweep garbage collector

* Every data structure is a digraph
    * Vertex = object
    * Edge = reference
* Roots: Objects known to be directly accessible by program (e.g. stack)  
* Reachable objects:
    * Objects indirectly accessible by program.
    * Starting at a root and following a chain of pointers.

## BFS in digraphs

* BFS is a digraph algorithm

* BFS (from source Vertex s)
    * Put s on to a FIFO queue, and mark s as visited. Repeat until the queue is empty.
    * Remove the least recently added vertex v
    * for each unmarked vertex pointing from v:
      add to queue and mark as visited.

## BFS in digraphs application: web crawler

* Goal: Crawl web, Starting from some root web page, `www.princeton.edu`

# 13.D Topological Sort

## Precedence scheduling

* Goal: Given a set of tasks to be completed with precedence constraints, which order should we schedule the tasks?

## Topological sort

* DAG: (Directed acyclic graph)
* Topo sort: Redraw DAG so all edges point upwards
* See the following code:
    * `DirectedCycle.py`
    * `DepthFirstOrder.py`

