
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

# Array problem with partial sum, always consider converting to pre-sum

*

# How to Ask questions to myself?

## `714_Best_Time_to_Buy_and_Sell_Stock_with_Transaction_Fee.py`
* Ask myself, when to start a new transaction? It has to be lower than last sales price `p-fee`
  Otherwise it's better to hold.

