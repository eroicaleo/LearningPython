# Chapter 01 Preliminaries

* `numpy`
* `pandas`
    * structured or tabular data
* `matplotlib`
* `Ipython` and `Jupyter`
* `Scipy`
* `scikit-learn`
* `statsmodels`
    * regression model

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
```

# Chapter 02 Basics, Ipython, Jupyter

* IPython can use <Tab> completion
* Use `?` for introspection: function/variables
    * Work both for IPython and Jupyter
* Use `??` for source code if possible
* Can use `?` to search namespace: `numpy.*load*?`
* `%run` to run scripts
* `%load` to be used in Jupyter notebook, to load a script to the code box
* `%run -i` to run scripts and it can access the variable already defined
* `%paste` and `%cpaste` to run the code from clipboard, cpaste looks more flexible
* Shortcuts: search `Ctrl-P`, `Ctrl-N`, `Ctrl-R`, delete current line `Ctrl-U`
* Magic commands (table 2-2 on page 47):
    * `%timeit`
    * `%debug`
    * `%pwd`
    * `%automagic`
    * `%magic`
* matplotlib integration
    * `%matplotlib` in Ipython
    * `%matplotlib inline` in Jupyter
* Python Basics
    * skip the bytes and unicode but may need to come back
    * skip the datetime but may need to come back

# Chapter 03 Built-in Data Types (skip for now)

# Chapter 04 Numpy basics

* `ndarray`, math functions, linear algebra, random generation, C API
* The reason `numpy` is fast `speed_test.py`:
    * store numbers in contiguous memory
    * operation on entire arrays without for loop
* It's generic multi-d for homogeneous data

### Creating ndarrays

* `np.array()`, accepts iterables
    * `arr1.ndim`
    * `arr1.shape`
    * `arr1.dtype`
* `ones, zeros, empty, full`, when create 2-d or higher, use tuple as the size.
   * The above 3 has `_like` version to create same size
* `arange` array version of `range`
* `asarray`: don't do anything, if input is already an array

### Data types

* When creating, do `dtype=float64` or `dtype=int32` 
* page 91, table 4-2 to summarize the data type
* `astype` to convert type
    * always create a new ndarray

### Arithmethic with numpy arrays

* The Arithmethic operations are element-wise

### Basic indexing

* 1-d is simple, pretty much like the python list. `basic_indexing.py`
* 1st distiction from python list, data is not copied, any modification goes to original array
    * Performance and memory consideration
    * If you need to get a copy, do `arr.copy()`
* 2-d can be indexed by
    * `arr2d[0, 2]`
    * `arr2d[0][2]`
* array can be indexing by slicing: `arr2d[2, :1], arr2d[:, :1]`

### Boolean indexing

* `bool_indexing.py`
* `data[names == 'Bob']`
* Select the inverse: `data[~(names == 'Bob')], data[np.logical_not(names == 'Bob')]`
* use `&` and `|` for and or
* Can also do `data[data < 0] = 0`

### Fancy indexing

* `fancy_indexing.py`
* Not like the slicing, always return a new array.
* Suprisingly, the following 2 are different:
    * `arr[[1, 5, 7, 2], [0, 3, 1, 2]]`
    * `arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]`

### Transposing and Swapping

* `transpose.py`
* `arr.T` for 2-d
* `arr.transpose((1, 2, 0))` means `arr[0, 1, 2]` becomes `arr.transpose((1, 2, 0))[1, 2, 0]`
* `arr.swapaxes(1, 2)` means `arr[0, 1, 2]` becomes `arr.swapaxes(1, 2)[0, 2, 1]`

## 4.2 Universal functions: Fast element-wise array function

* fast vectorized wrappers for simple functions `universal.py`
* `np.sqrt(arr) np.exp(arr) np.maximum(x, y) np.modf(arr)`
* Can also accept an `out` argument, so it's inplace.
* Table 4-3, 4-4 summarize the Universal functions

## 4.3 Array-Oriented Programming with Arrays

* They are called vectorization/broadcasting

### 4.3.1 condition logic as array

* `where.py`
* Given condition array, choose from xarr when condition is true, otherwise choose from yarr
* `np.where(arr > 0, 2, -2)` or `np.where(arr > 0, 2, arr)`

### Mathematical and Statistical Methods

* `math_stat.py` 
* `mean, sum`
    * The `axis` argument takes 1 integer or a tuple
    * So `arr3d.mean(axis=0)` means for the (0, 0) element, is to average `arr3d[:,0,0]`
* Table 4-5 summarize the the math functions

### Methods for Boolean Arrays

* `bool_array.py`
* `any()` and `all()`

### Sort

* sort is in-place, can be across axis for higher dimen

### Array unique set logic

* Table 4.6 `unique, intersect1d, in1d, union1d, setdiff1d, setxor1d`
* The `1d` means the results are in 1-d array, the argument can be 2-d/3-d

## Skip 4.4 - 4.8

# Chapter 04 Getting Started with pandas

## 5.1 Introduction to pandas Data Structures

### Series

* It has values and index: `obj.values, obj.index`
* Use numpy functions, filtering with Boolean array, scalar multi, applying math function
  preserve the index-value link.
* Another way to think is fixed-length, ordered dict.
* It's OK to convert dict to `np.Series`
    * We can override the key by passing the `index` argument.
* `pd.isnull, pd.notnull` to detect missing value.
* Automatic align by index label for Arithmethic operations.
* `Series` and index all have `name` attr

### DataFrame

* `DataFrame.py`
* Most common way: dict of equal length lists or np arrays to `pd.DataFrame`
    * index are assigned automatically, index can be rename by `index` argument
    * column are placed in sorted order, can be changed by specifying `columns` argument
    * `head()` to show top 5
    * For column name doesn't exist, create with `NaN`
* `frame.columns` is a index object
* a column can be accessed by dict like notation or attribute
    * The return value is a `Series` object
* a row can be accessed using `loc`, like `frame.loc['three']`
* a column can be assigned by a scale or an array, but the length must the same
    * If assign a `Series`, the labels must be aligned
* assign column not exist will create new column
* `del` will delete a column
* Another common way: dict of dicts, the outer one will be column, the inner one will be rows
    * Can be transpose by `T`
* 3rd way is dicts of Series, complete list of construction see table 5.1
* DataFrame has attribute: `columns`, `index`, they both have `name` attr.
* DataFrame also has `values` attribute: which is a 2-d `np.array`

### Index object

* `Index.py`
* Index object holds axis labels and other meta data
* It's immutable
* Can be created by `pd.Index(np.arange(3))`
* `Index` is like a fixed size set, but can have duplicate elements
* Table 5.2 summarize the `Index` method.

## 5.2 Essential Functionality

### Reindexing

* `reindexing.py`
* It will change the order of indexing, if there is new label, it will assign `nan`
* interpolation method, use `method` argument:
    * `ffill`, forward fill
* when reindex columns of a frame, do `frame.reindex(columns=)`
* A lot of users prefer to use `.loc` to reindexing.
* Table 5.3 reindexing func argument

### Dropping Entries from an Axis

* `dropping.py`
* To drop a column in data frame, use `axis=1` or `axis='columns'`
* drop can be inplace, but the original data is destroyed.
