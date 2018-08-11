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
    * `arr[[1, 5, 7, 2], [0, 3, 1, 2]]`, this one is [arr[1, 0], arr[5, 3], arr[7, 1], arr[2, 2]]
    * `arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]`, this one is 4x4 array

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

### Indexing, Selection, and Filtering

* `indexing.py`
* Can use Series's index/label or number
* slicing with label include the end label
* `loc` and `iloc` to select rows
    * Also works with slicing
* Table 5-4 to summary the indexing options

### Integer Indexing

* `integer_indexing.py`
* Using `ser[-1]` with `ser = pd.Series(np.arange(3.))` raise an exception
* Using `ser2[-1]` with `ser2 = pd.Series(np.arange(3.), index=list('abc'))` raise an exception
* This is because when labels are all integers, it will cause confusion. But if labels are
  non integers, there is no confusion.
* In the first case, we need to use `ser.iloc[-1]`

### Arithmetic and Data Alignment

* `align.py`
* Adding up objects, the index in the results will be the union of the index pairs
    * If one index is missing in another, it will be `NaN`
* For data frame, the alignment happens for both columns and indexes
* Because by default, the missing value will be `np.nan`. If we want to a default value,
  we need to use `df1.add(df2, fill_value = 0)`
* In addtion to `add`, we also have `radd`. Table 5-5 summarize the methods.
* `reindex` also has a `fill_value` argument.
* For `np.arrary`, there is broadcasting. `DataFrame` and `Series` works similarly.
    * By default, arithmetic between DataFrame and Series matches the index of the Series on the DataFrame’s columns, broadcasting down the rows.
    * If an index value is not found in either the DataFrame’s columns or the Series’s index, the objects will be reindexed to form the union
    * If we want to do broadcast over columns, we have to use method and do `axis=0` or `axis='index'`

### Function Application and Mapping

* `func_app_map.py`
* Universal functions for `np.array` also works for `Series` and `DataFrame`.
* Another frequent operation is applying a function on 1-d arrays to each row or column: `apply` 
    * Default is applying the function on each columns
    * For row, we need to do `DataFrame.apply(f, axis='columns')`
* Many `np.array` functions are also `DataFrame` functions, e.g. `mean` and `sum` so no need to call `apply`
* The applied function doesn't have to return a scalar value, it can return a `pd.Series`
* Element-wise function needs to use `applymap`, which is similar to `pd.Series.map`

### Sorting and Ranking

* `sort.py`
* sort based on index: `pd.Serie.sort_index()` or `pd.Series.sort_index()`, `axis=1` for `columns`
    * `ascending=False`
* sort by values: `sort_value()`
    * Missing values are at the end
* sort by values for `DataFrame`, we can use the values in one or more columns: `frame.sort_index(axis=1).sort_values(by=['a', 'b'])` .
* `rank` function assign the ranks, by default, for tie, it assigns the mean value.
    * For tie, can also based the appreance first `method='first'`
    * For tie, can also have `method='max'`
    * Table 5-6 summarize tie-breaking

### Axis Indexes with Duplicate Labels

* `dup_index.py`
* `pd.Index.is_unique` tells if the index is unique, its an attribute
* The duplication makes code more complicated

## 5.3 Summarizing and Computing Descriptive Statistics

* `summ_stat.py`
* across columns: `pd.DataFrame.sum(axis='columns')`
* By default, NaN is skipped. Don't skip NaN: `pd.DataFrame.sum(axis='columns', skipna=False)`
* Table 5-7 summarize options for reduction methods
* Non-reduction methods: `idxmax/idxmin`, `cumsum`, `describe`
* Table 5-8. Descriptive and summary statistics

### Correlation and Covariance (skip for now due to don't have dataset)

### Unique Values, Value Counts, and Membership

* `uniq_count_mem.py`
* `unique()`
* `obj.value_counts()` and `pd.value_counts(obj.values)`
* `obj.isin(['b', 'c'])`
* related: `Index.get_indexer`, see the sample code
* Table 5-9 summarize these methods
* `pd.DataFrame.fillna(0.0)` will fill the `NaN` with 0.0

# Chapter 06 Data Loading, Storage, and File Formats (skip for now) 

# Chapter 07 Data Cleaning and Preparation
