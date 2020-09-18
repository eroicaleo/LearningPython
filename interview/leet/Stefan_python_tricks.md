
## if-else trick

### `331_Verify_Preorder_Serialization_of_a_Binary_Tree.py`

* See how stefan implements the following:

```python
# Regular way
if val == '#':
    need -= 1
else:
    need += 1

# Stefan's way
need -= ' #'.find(val)
```

## Regular expression trick

### How to use the captured pattern in replacement

* Normally, in the python doc, we would use `\g<name>, \g<1>, \1`
  see `(?P<name>...)` in [here](https://docs.python.org/3/library/re.html)
* But in Problem `394_Decode_String`, here is how Stefan use

```python
s = re.sub(r'(\d+)\[([a-z]+)\]', lambda m: int(m.group(1)) * m.group(2), s)
```

## `list` tricks

### `index`

* If a value is not in a list, then `[1].index(0)` raise an `ValueError`.
* In Problem `047_Permutations_II`, Stefan uses a sentinel to guarantee
  `(p+[n]).index(n)` does raise exception.

```python
perms = [p[:i]+[n]+p[i:] for p in perms for i in range((p+[n]).index(n)+1)]
```

* Here is another example to add a sentinel at the end of list: `436_Find_Right_Interval.py`
  here we need to use `bisect_left`, if an element is bigger than all elements in the list,
  `bisect_left` returns the length of the list. However, the question asks to return
  an -1.

```python
    def findRightInterval_Stefan(self, intervals):
        left_list = sorted([(i[0], n) for n, i in enumerate(intervals)]) + [(math.inf, -1)]
        return [left_list[bisect_left(left_list, (i[1], 0))][1] for i in intervals]
```

### slicing

* Let `stack = [1,2,3,4,5]`, `stack[:-1]` gives `[1,2,3,4]` and so on
  but stack[:-0] gives `[]`, what if we want the whole list?
* We can do this `stack[:-0 or None]`
* Stefan's solution in `402_Remove_K_Digits.py`

## `functools` tricks

### `reduce`

* Sometimes, e.g. `047_Permutations_II`, we will see this kind of code when we use bottom-up
  approach to build something, `reduce` can make it one-liner.
  See the `functools.reduce(function, iterable[, initializer])`
  [official doc](https://docs.python.org/3/library/functools.html#functools.reduce)

```python
perms = [[]]
for n in nums:
    perms = [p[:i]+[n]+p[i:] for p in perms for i in range((p+[n]).index(n)+1)]
return perms

from functools import reduce
return reduce(lambda perms, n: [p[:i]+[n]+p[i:] for p in perms for i in range((p+[n]).index(n)+1)], nums, [[]])
```

### `any`

* Sometimes, I would like to see if any of the iterable is `True`

```python
# My way
for c in path:
    if c != self.word_end:
        ret = ret or self.search_recursive(word[1:], path[c])
    if ret:
        return ret
return ret

# Stefan's way
if word[0] == '.':
    return any(self.search_recursive(word[1:], path[c]) for c in path if c != self.word_end)
```

### `filter`

* How to filter `None`: `211_Add_and_Search_Word.py`
* See discussion of [here](https://stackoverflow.com/questions/16096754/remove-none-value-from-a-list-without-removing-the-0-value)

```python
filter(None, iterable)
```

### `iter`

* `392_Is_Subsequence.py`

```python
t = iter(t)
return all(c in t for c in s)
```

## bit manipulation tricks

### how to get the right most bit that's 1'b1: `260_Single_Number_III.py`

```python
diff &= -diff
```

## Breadth first implementation

* `211_Add_and_Search_Word.py`
* My lame implementation:

```python
def search_iterative(self, word):
    nodes = [self.word_dict]
    for c in word:
        new_nodes = []
        for n in nodes:
            if c in n:
                new_nodes.append(n[c])
            elif c == '.':
                for k in n:
                    if k != self.word_end:
                        new_nodes.append(n[k])
        nodes = new_nodes
    return any(self.word_end in n for n in nodes)
```

* Stefan's

```python
def search_iterative2(self, word):
     nodes = [self.word_dict]
     for c in word:
         nodes = [kid for n in nodes for kid in
                         ([n[c]] if c in n else
                          [n[k] for k in n if k != self.word_end] if c == '.' else [])]
     return any(self.word_end in n for n in nodes)
```

## `itertool`

### `zip_longest`: `165_Compare_Version_Numbers_short.py`

```code
v1, v2 = zip(*itertools.zip_longest(v1, v2, fillvalue = 0))
```

### `heap` problems

## Heap
