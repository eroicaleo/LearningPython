arr = ['one', 'two', 'three']
print(arr[0])
# Lists have a nice repr:
print(arr)
# Lists are mutable:
arr[1] = 'hello'
print(arr)

del arr[1]
print(arr)

# Lists can hold arbitrary data types:
arr.append(23)
print(arr)

print('#' * 80)
print('# tuple')
print('#' * 80)
arr = 'one', 'two', 'three'
print(arr[0])
# tuple have a nice repr:
print(arr)

# Tuples are immutable:
try:
    arr[1] = 'hello'
except TypeError as e:
    print(e)

try:
    del arr[1]
except TypeError as e:
    print(e)

# Tuples can hold arbitrary data types:
# (Adding elements creates a copy of the tuple)
print(arr + (23,))
