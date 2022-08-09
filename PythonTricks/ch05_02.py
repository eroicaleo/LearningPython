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

import array
arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])
print(arr)
arr[1] = 23.0
print(arr)
del arr[1]
print(arr)
arr.append(42.0)
print(arr)
try:
    arr[1] = 'hello'
except TypeError as e:
    print(f'Trying to assign a string to a floating array failed: {e}')

arr = 'abcd'
print(arr[1])
try:
    arr[1] = 'e'
except TypeError as e:
    print(f'Trying to assign a new value to an element failed: {e}')

try:
    del arr[1]
except TypeError as e:
    print(f'Trying to delete an element failed: {e}')

print(list(arr))
print(type('abc'))
print(type('abc'[0]))

