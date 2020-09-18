
# Reverse thinking

## `316_Remove_Duplicate_Letters.py`

* Move letter backward is not working, why not try to move letter forward

## `417_Pacific_Atlantic_Water_Flow.py`

* Flow from inside out is working, why not flow from outside in?

## `407_Trapping_Rain_Water_II.py`

* Flow from inside out is working, why not flow from outside in?

## `312_Burst_Balloons.py`

* `i` is the first balloon to pop doesn't work, why not make `i` the last.

## `282_Expression_Add_Operators.py`

* Build the anwser from bottom up doesn't work, why don't consider
  build the anwser from top down

### `174_Dungeon_Game.py`

* My first thinking is from [0,0] to [nr-1,nc-1], but turns out the correct way is
  from [nr-1,nc-1] to [0,0].

## `274_H_Index.py`

* Sort citations from low to high makes the code ugly, why don't sort from high to low.

## `456_132_Patterns.py`

* Start from head is hard, starting from the end is easier.

## `503_Next_Greater_Element_II.py`

* Start from first element is hard, but start from the last element is much cleaner.

# Array problem with partial sum, always consider converting to pre-sum

*

# How to Ask questions to myself?

## `714_Best_Time_to_Buy_and_Sell_Stock_with_Transaction_Fee.py`
* Ask myself, when to start a new transaction? It has to be lower than last sales price `p-fee`
  Otherwise it's better to hold.

# Step by Step thinking (循序渐进，从问题复杂度的纬度)

* In this process, when we try to reduce one order, we usually have to trade time with space.

* `456_132_Patterns.py` by Fun4leetcode
    * It starts with O(n^3) solution then goes to O(n^2) solution, then goes to 2-pass O(n^1) solution
      then goes to 1-pass O(n) solution
    * It also uses the Reverse thinking.

* `421_Maximum_XOR_of_Two_Numbers_in_an_Array.py`
    * The naive approach is `O(n^2)`
    * If we build a trie for all numbers in the first pass
    * In the 2nd pass, we find which number in the trie can produce the `max_xor` with current number.

# Step by Step thinking (循序渐进，从问题规模的纬度)

* `421_Maximum_XOR_of_Two_Numbers_in_an_Array.py`, Stefan's solution, assume we have
  the max for the first 7-bit, how do you find the max for the first 8-bit?

* In general, DP falls into this category.
