
* We want the DFS have the following property
  start from one node which has certain property,
  every node can be reached through DFS have the same property.
  For example, in `417_Pacific_Atlantic_Water_Flow.py`,
  If we start from the ocean side, then we know every node
  we travel connect to the ocean. But if we start from
  some node in the middle, we don't have such property.

* In the DFS, when we see a visited node which is in the upper
  level of the stack, we cannot visit it again.
  But we need to ask, if we don't visit it, will we get the
  valid solution. E.g., in `329_Longest_Increasing_Path_in_a_Matrix.py`
  it is this case. Because if one node is in upper level of the stack
  it must be smaller than current value, we cannot visit again.
  So even without visit it, the solution is still optimal. 

# For example: `417_Pacific_Atlantic_Water_Flow.py`

