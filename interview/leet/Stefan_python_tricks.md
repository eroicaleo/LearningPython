
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
