
* We need to find sub-problems that is disjoint/irrelevant to each other
* We need to find what's the expectation of each recursive call
* Some problem needs to find some optimal solution
    * `761_Special_Binary_String.py`
    * In this problem
* Some problem needs to find all solutions satisfying certain conditions
    * `301_Remove_Invalid_Parentheses.py`

# The recursive call on strings

* Typical problems
    * `394_Decode_String.py`
    * `761_Special_Binary_String.py`
    * `224_Basic_Calculator.py`
* Similar problems but has a tree context
    * `1008_Construct_Binary_Search_Tree_from_Preorder_Traversal.py`, lee315's solution
    * `105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.py`
      my own solution and Stefan's solution

## Recursive approach

* This kind of problems normally have some kind of level concept
    * for example: S = '1100' = '(())' has 2 levels
    * S = "11011000" = '(()(()))' has 3 levels: '(......)', '.()(()).', '....()..'
    * s = "3[a2[c]]" has 3 levels
    * s = "3[a]2[bc]" has 2 levels
* The normal pattern is:
    * We have an instance variable `i` to travel through the string
      it will get increased in recursive call
    * Use while loop and check `i < len`
        * read the character and increase self.i
        * One `if` branch to go down
        * One `else` branch to break while loop and go up
    * We need to figure out which char makes us go down one level, which makes us go up one level
      it is usually pretty obvious, `[` to go down, `]` to go up. `1` to do down and `0` to go up
    * We need to be clear on what do we expect to return from the recursive call.
      it is usually the solution of the sub-problem.
          * E.g., S = "11011000" = '(()(()))', when we call at position 0, it's the solution to entire problem
          * when we call at position 1, it should return `()(())`. In fact, since it will return only when it
            sees the `)` that matches the `(` in position 0, it should return `(()(()))`.
    * One IMPORTANT POINT, at current level, when we see the symbol, e.g `(`, to go down one level, when we return
      from the recursive call, the index is right after the matching symbol, e.g. `)`.
      In some case, we still need the matching symbol, e.g. problem `761`, then we need to take care of this.
      We can either take care of it in the recursive call the level below, like the v2 version of `761`
      or the current level, like the v3 version of `761`
    * At current level, when we return from the recursive call, and before we return, we need to
      to do some processing, `394` needs to concat strings, `761` needs to sort all same level string

## Iterative approach

* Use a stack
* Use `for` loop to go through the string
* When see go down symbol, push the current level thing into stack
* When see go above symbol, process the current level, combine with upper level

## Comparison between recursive and iterative code

* `394_Decode_String.py`
* `224_Basic_Calculator.py`
* When the char is not go-down or go-up, the code are exactly the same
    * `if c.isdigit():` and `elif c == '+' or c == '-':`
* The initialization in the `dfs` are exactly the same as the one in iterative method
  at the beginning and the one when it encounters the go-down symbol.
* The thing returned from `dfs` and iterative method are the same.

```python
    def calculate(self, s: str) -> int:
        self.index, l = 0, len(s)
        def dfs():
            n, res, last_op = 0, 0, '+'
            while self.index < l:
                c, self.index = s[self.index], self.index+1
                if c.isdigit():
                    n = 10*n+int(c)
                elif c == '+' or c == '-':
                    n, res, last_op = 0, res+n if last_op == '+' else res-n, c
                elif c == "(":
                    n = dfs()
                elif c == ")":
                    break
            return res+n if last_op == '+' else res-n
        return dfs()

    def calculate_iter(self, s: str) -> int:
        stack = []
        n, res, last_op = 0, 0, '+'
        for c in s:
            if c.isdigit():
                n = 10*n+int(c)
            elif c == '+' or c == '-':
                n, res, last_op = 0, res+n if last_op == '+' else res-n, c
            elif c == "(":
                stack += [res, last_op]
                n, res, last_op = 0, 0, '+'
            elif c == ")":
                res += (n if last_op == '+' else -n)
                n, last_op, res = res, stack.pop(), stack.pop()
        return (res + (n if last_op == '+' else -n))
```

# recursive call to build anwser from top down

* This kind of problems aim to build a set of solutions that
  satisfy certain criterion, it builds from top down, and
  at certain recursive call, we might encounter a valid solution,
  we add it to the solution set.

* `301_Remove_Invalid_Parentheses.py`
* `282_Expression_Add_Operators.py`

* `Subsets II`

```python
res = []
nums = sort(nums)

def rec(i, path):
    res.append(path)
    for j in range(i, len(nums)):
        if j > i and nums[j] == nums[j-1]:
	    continue
        rec(j+1, path+[nums[j]])
rec(0, [])
return res
```

* `40_Combination_Sum_II.py`
