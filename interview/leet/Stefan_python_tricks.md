
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
