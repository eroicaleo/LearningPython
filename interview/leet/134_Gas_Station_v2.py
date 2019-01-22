#!/usr/bin/env python

# Based on the highest voted solution from discussion
# proposition 1:
# If the total number of gas is bigger than the total number of cost.
# There must be a solution.
# Proof: by induction
# Suppose n stations and the proposition is true, and you have n+1
# stations. Find the n stations, which sum is > 0,
# i_0, ..., i_j, i_(j+1), ..., i_n

# Proof: from any node i0, go clockwise to i1, such that i1 is the
# first station sum(a[i0:i1]) < 0, then start from next station of i1
# to i2, such that sum(a[i1+1:i2]) < 0, continue this process until
# we pass through i0, we can not stop at any where between i0 and i1
# because if stops at i0 < ik < i1, it's a contradiction. Because, we
# assume i1 is the first station such that sum(a[i0:i1]) < 0.
# Now we have a disjoint set of segments such that it covers all stations
# And each of them has negative sum, which contradicts the
# all sums is > 0

class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
 
