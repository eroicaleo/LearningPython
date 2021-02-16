
# Use array as an hash

* Some problems asks us to find something in one array
  and it can only run on `O(n)` and constant space.
* In order to search something, we need `O(n)` time to build a hash table
  then the hash table takes `O(n)` space.
* So we can use the existing array as a hashtable, use the index as the key

## `41_First_Missing_Positive.py`

* We want to use the original array `nums` as a hashtable, and when we see `i`,
  we want to somehow mark `nums[i]`.
* But since `nums[i]` itself contains a number and we don't want to lose that number
  so we make the sign of it to negative, this way, we know `i` is presented in the array.
* So now, we must make sure before processing, nums[i] is all positive
* See the `firstMissingPositive_2.py`
