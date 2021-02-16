
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
  按照这样的思路，可以理解成DP像是一种数学归纳法.

* Examples are: 
    * Longest common substring
    * Longest common subsequence
    * `115_Distinct_Subsequences.py`

# `115_Distinct_Subsequences.py`

* How to divide the solution to disjoint sub-problems
* what is the meaning of dp[i, j]: how many subsequence of s[:j] matches t[:i]

# `123_Best_Time_to_Buy_and_Sell_Stock_III.py`

* To solve this problem, it's helpful to consider a simplified problem:
    * what if we are only allowed to buy/sell at most one time.
    * Then it's easier to come up with DP solution with one row.
    * Then in the next step, we extend to 2 row to solve buy/sell at most two times.
* For better understanding, this problem has buy and sell 2 operations, so we create 2 DP tables, `dpbuy` and `dpsel`
* what is the row in dpsel: the ith sell
* what is the row in dpbuy: the ith buy
* what is the col: the price on each day
* what is the meaning of dpbuy[i, j]: the max money when finish the ith buy  before or at day j
* what is the meaning of dpsel[i, j]: the max money when finish the ith sell before or at day j
* After 2nd round, and after working on some other stock problems
  I think the better way to understand the `dpbuy[i, j]` and `dpsel[i, j]` would be:
    * `dpbuy[i, j]`: the max money we can have at ith buy operations when we hold a stock at day j
    * `dpsel[i, j]`: the max money we can have at ith sell operations when we don't hold a stock at day j
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

# `312_Burst_Balloons.py`

* We construct a 2-d DP, in the DP table, `dp[l][r]` is the max coins we can get when popping [l+1,r-1]
* The relation is assume j is the last one to pop, then the coin is we get is `nums[j]*border+dp[j][r]+dp[l][j]`

```
dp[l][r] = max(nums[j]*border+dp[j][r]+dp[l][j] for j in range(l+1,r))
```

```python
3 1 5 8
1 3 1 5 8 1
```

* Assume 8 is the last popped, then `dp = [x, x, x, 8]`
* Assume [5,8] is the last popped, then `dp = [x, x, 48, 8]`

* Step 1

   1   3   1   5   8   1
1          3             
3              15        
1                  40    
5                      40
8             
1             

* Step 2
    * `dp[0][3] = max(dp[1][3]+nums[0]*nums[1]*nums[3], dp[0][2]+nums[0]*nums[2]*nums[3]) = max(15+15, 3+5) = 30`
    * `dp[1][4] = max(dp[2][4]+nums[1]*nums[2]*nums[4], dp[1][3]+nums[1]*nums[3]*nums[4])`
    * `dp[2][5] = max(dp[3][5]+nums[2]*nums[3]*nums[5], dp[2][4]+nums[2]*nums[4]*nums[5])`

   1   3   1   5   8   1
1          3   30        
3              15        
1                  40    
5                      40


* Step 3

  1 3 1 5  8 1
1 
3   3        
1   4 1      
5     6 5    
8       48 8  
1            

# Palindromic problems

* `5_Longest_Palindromic_Substring.py`

This problem construct DP table from bottom right corner to the top row.
