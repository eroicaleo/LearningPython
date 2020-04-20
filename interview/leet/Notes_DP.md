
# One point of view, in the problem there are some sequence of operations

* DP problem must have some kind of sequence, and this sequence normally consists of y-axis:
    * Shoot bullooms
    * Rob houses
    * Sell stocks
    * Matching characters
* For DP problem, always answers the following 4 questions:
    * what is the meaning of row:
    * what is the meaning of col:
    * what is the meaning of dp[i, j]:
    * what is recurrance relation dp[i, j]:
	* how to divided dp[i, j] into disjoint categories:
	* For example: when it's a sequence of operations, we can divide by do we do this operations or not
	  like, do we rob house j or not? Do we sell stock on day j?
* Consider Further optimization
* Boundary conditions
    * Does adding Ф help? like `044_Wildcard_Matching.py` and all other string problems
    * Don't start on column 0
* If the space can be improved to O(MN) to O(N)
* If the space can be further reduced to O(1), like
    * `123_Best_Time_to_Buy_and_Sell_Stock_III.py`? If we don't go row by row, but go column by column

# Another point of view, the current problem can be divided into disjoint sub-problems

* Examples are: 
    * Longest common substring
    * Longest common subsequence
    * `115_Distinct_Subsequences.py`

# `115_Distinct_Subsequences.py`

* How to divide the solution to disjoint sub-problems
* what is the meaning of dp[i, j]: how many subsequence of s[:j] matches t[:i]

# `123_Best_Time_to_Buy_and_Sell_Stock_III.py`

* For better understanding, this problem has buy and sell 2 operations, so we create 2 DP tables, `dpbuy` and `dpsel`
* what is the row in dpsel: the ith sell
* what is the row in dpbuy: the ith buy
* what is the col: the price on each day
* what is the meaning of dpbuy[i, j]: the max money when finish the ith buy  before or at day j
* what is the meaning of dpsel[i, j]: the max money when finish the ith sell before or at day j
* what is recurrance relation `dpbuy[i,j] = max(dpbuy[i, j-1], dpsel[i-1, j-1]-price[j])`
    * how to divid dpbuy[i, j] into disjoint categories:
       1. We don't buy on day j, in this case: `dpbuy[i, j] = dpbuy[i, j-1]`
       2. We buy on day j, in this case: `dpbuy[i, j] = dpsel[i-1, j-1]-price[j]`
*  what is recurrance relation `dpsel[i,j] = max(dpsel[i, j-1], dpbuy[i-1, j-1]+price[j])`
    * how to divid dpsel[i, j] into disjoint categories:
       1. We don't sell on day j, in this case: `dpsel[i, j] = dpsel[i, j-1]`
       2. We sell on day j, in this case: `dpsel[i, j] = dpbuy[i-1, j-1]+price[j]`
* Boundary conditions optimization
    * dpbuy[i, 0] = -price[0]
    * dpsel[i, 0] = 0, since we cannot sell at time 0
* Memory optimization from O(MN) to O(N)
    * Since dpbuy[i,j] and dpsel[i,j] only depends only on current row and previous row
      so the memory can be reduced to O(N)
* Memory optimization for O(N) to O(1)
    * We update across the row, since it only has 2 transaction

# `213_House_Robber_II.py`
* what is the row: the house in it's door number
* what is the col: the ith robbery
* what is the meaning of dp[i, j]: the max money can get after jth robbery and the robbered house number is <= i
* what is recurrance relation dp[i, j] = max(dp[i-1, j], dp[i-2, j-1]+nums[i], dp[i,j-1])
    * how to divided dp[i, j] into disjoint categories:
        1. house i has been robbed in previous round, so it's dp[i,j-1]
        2. we don't rob house i in round j, i.e. dp[i-1, j]
        3. we rob house i in round j, i.e. dp[i-2, j-1]+nums[i]
