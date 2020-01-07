# Some Reference

* [Select and Indexing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)

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
* Using `ser2[-1]` with `ser2 = pd.Series(np.arange(3.), index=list('abc'))` won't raise an exception
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

## 7.1 Handling Missing Data

* `np.nan` is a `float` type, it's a sentinal value.
* `isnull()` to tell if it's `nan`
* `None` is also treated as `nan`
* Table 7-1, NA Handling methods: `dropna/fillna/isnull/notnull`

### Filtering Out Missing Data

* `filter_out.py`
* By default, `dropna` for `DataFrame` will drop the any rows containing `NA` 
* Need to do: `data.dropna(how='all')`
* To drop column, `data.dropna(axis=1)`
* Use `df.dropna(thresh=2)` to drop only some of the `NA`

### Filling in Missing Data

* `fill_in.py`
* df.fillna(0), can accept a `dict`
* If want to inplace, then `_ = df.fillna(0, inplace=True)`
* Can use the method for reindexing, `df.fillna(method='ffill', limit=2)`
* Table 7-2. fillna function arguments

## 7.2 Data Transformation

### Removing Duplicates

* `remove_duplicates.py`
* `data.duplicated()` tells if a row is a duplication of one of previous rows
* `data.drop_duplicates()` to drop them, `keep='last'`

### Transforming Data Using a Function or Mapping

* `Series.pd.map` takes a dictionary argument: `lowercased.map(meat_to_animal)`
* It can also just take a function: `data['food'].map(lambda x: meat_to_animal[x.lower()])`

### Replacing Values

* `replace.py`
* `pd.Series.replace()` can use `inplace=True`
* If want to replace multiple values to the same value, then pass a list
* If want to replace multiple values to different value, then pass 2 lists or a dictionary

### Renaming Axis

* `rename_axix.py`
* The `Index` object also has a `map` method
* If we want to create a new DataFrame, use `data.rename(index=, columns=)`
    * the argument can either take a function or a dictionary.
    * can have `inplace=True`

### Discretization and Binning

* `discretize_bin.py`
* `cats = pd.cut(ages, bins)`
    * Note that if a value is out of the range, when you print `cats`, it shows up as `NaN`
    * When you print `cats.codes`, it shows up as `-1`
* It is a `Categories` object.
* To find the levels: `cats.codes`
* To find the Categories: `cat.categories`
* Count each level: `pd.value_counts(cats)`
* Default is left exclusive / right inclusive, to change this behaviour: `pd.cut(ages, bins, right=False)`
* To give each bin their names: `cats_new = pd.cut(ages, bins, labels=group_names)`
* If pass a integer to `bins` argument, it will split equal distance based on min/max
* `qcut` based on quatile, so each has roughly the same number of samples
    * We can pass our own `quatile` to `qcut`

### Detecting and Filtering Outliers

* `outliers.py`
* `data.describe()` to get a summary of the DataFrame.
* find all rows with any of element whose absolute value is greater than 3
  `data[(np.abs(data) > 3).any(1)]`
* cap it at +/-3.0: `data[np.abs(data) > 3] = np.sign(data) * 3.0`

### Permutation and Random Sampling

* `permutation.py`
* Generate the `sampler = np.random.permutation(n)`
* `df.take(sampler)` to permutate the row
* `df[sampler]` to permutate the column
* `df.sample(n)` to select a random subset across the row, but you can do it across columns by doing
  `df.sample(n, axis=1)`, note this doesn't have repeat choice
* To have repeat choice, do `df.sample(n, replace=True)`

### Computing Indicator/Dummy variables

* `indicator.py`
* What a indicator or dummy matrix? If a column with k values, convert it to a matrix with k column
* `pd.get_dummies(df['key'])`
* Add a prefix: `pd.get_dummies(df['key'], prefix='key')`
* Join the dummy matrix, with previous column `df_with_dummy = df[['data1']].join(dummies)`
    * Note1: `df[['data1']]` creates a DataFrame, `df['data1']` creates a Series.
    * Note2: `pd.DataFrame.join` to merge 2 DataFrame by `index`
* For the previous example, the `key` can take one of `a, b, c`.
  But for Movie genres, one move can be action, comedy and children's at the same time
* Then we need to do it in several steps:
    * Create a list of all genres:
```python
all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
```
    * Create a all zero matrix: `zero_matrix = np.zeros((len(movies), len(genres)))`
    * And create a DF based on the zero matrix: `dummies = pd.DataFrame(zero_matrix, columns=genres)`
    * iterate each movie, find it's genres, assign them to 1. We use `get_indexer`.
```python
for i, gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indices] = 1
```
* A common recipe is with `cut`: `pd.get_dummies(pd.cut(values, bins))`

## 7.2 String Manipulation

### String Object Methods 

* `string_object_methods.py`.
* See table 7-3 for a reference.

### Regular Expressions

* `regular_exp.py`
* `pattern.split(text)`
* `pattern.findall(text)`
* `pattern.search(text)`
* `pattern.match(text)`
* `pattern.sub(repl, text)`

### Vectorized String Functions in pandas

* `vectorized_string.py` 
* Some value maybe `np.nan`, `pd.Series.map` can't handle NA values.
* Have to use `pd.Series.str` function
    * It can also use Regular expression
* `data.str.get(1)`, `data.str[1]`, `data.str[:5]`
* erreta/typo here
* See table 7-5 for a reference

# Chapter 08 Data wrangling: Join, Combine, Reshape

## 8.1 Hierachical Indexing

* `hier_index.py`
* Indexing example: `Notes_indexing.md`
    * section "Indexing in Hierachical Series"
    * section "Indexing in Hierachical DataFrame"
* The hierachical Series can be converted to `DataFrame` and back
    * `data.unstack()`
    * `data.unstack().stack()`
* For hierachical `DataFrame`, the levels can assign name:
    * `frame.index.names = ['key1', 'key2']`
    * `frame.columns.names = ['state', 'color']`
* `pd.MultiIndex` can be created alone:
    * `mi = pd.MultiIndex.from_arrays([['Ohio','Ohio','Colorado'], ['Green','Red','Green']], names=['state', 'color'])`

### 8.1.2 Reordering and Sorting Levels

* `reorder_sort_levels.py`
* swap the across the row index can be name based and level based
    * `frame.swaplevel('key1', 'key2')`
    * `frame.swaplevel(0, 1)`
* swap the across the column need to add `axis=1`
    * `frame.swaplevel('state', 'color', axis=1)`
    * `frame.swaplevel(0, 1, axis=1)`
* sort index across the row
    * `frame.sort_index(level=1)`
* sort index across the column
    * `frame.sort_index(level=0, axis=1)`

### 8.1.3 Summary Statistics by Level 

* `summ_stat_by_level.py`
* Most statistic functions takes the `level` argument
* You can also use `axis`

### 8.1.4 Indexing with a DataFrame’s columns

* `index_df_col.py`
* We want to use one or more columns as the index or vice versa
* use `set_index`: `frame.set_index(['c', 'd'])`
* use `reset_index` to do the reverse

## 8.2 Combining and Merging Datasets

* [official examples](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)

### 8.2.1 Database-Style DataFrame Joins

* `db_style_df_join.py`
* Use `pd.merge()` function to do many-to-one join
    * It's a good practise to specify the merge key explicitly, like `pd.merge(df1, df2, on='key')`
    * If there is no column with the same name, then we have to specify the left key and the right key
      `pd.merge(df1, df2, left_on='lkey', right_on='rkey')`
    * Note, if one value in the merge column exists in one dataframe but not in the other, it will
      be dropped.
    * The above behavior is called `inner`, other 3 options are `left/right/outer`
* Use `pd.merge()` function to do many-to-many join, which is like Cartesian product
    * `pd.merge(on=['key1', 'key2'])` to supply a list of keys
    * treat overlapping column name by supplying a list of name, `pd.merge(on='key1', suffix=['_left', '_right'])`
* See table 8-2 for reference

### 8.2.2 Merging on Index

* `merge_on_index.py`
* In some cases, the merge key will be in the index, we need to use `left_index=True` or `right_index=True` or both
    * `pd.merge(left=left1, right=right1, left_on='key', right_index=True)`
    * `pd.merge(left=left1, right=right1, left_on='key', right_index=True, how='outer')`
* Hierarchical index is more complex, has to pass a list for `left_on` or `right_on`
    * `pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')`
* Both dataframe can use index to merge
    * `pd.merge(left2, right2, how='outer', left_index=True, right_index=True)`
* If 2 dataframe has similar index, then we case use `join` method
    * `left2.join(right2, how='outer')`
    * `left1.join(right1, on='key')`
* `join` index-on-index merge, we can give a list of dataframe:
    * `left2.join([right2, another], how='outer')`

### 8.2.3 Concatenating Along an Axis

* `concat.py`
* It has been called concatenation, binding or stacking.
* `np.concatenate([arr, arr], axis=1)` will concat along column
* `np.concatenate([arr, arr], axis=0)` will concat along row
* For a concat of `Series` with index, and when we concat along the column, the default
  behaviour is to use `outer` method for the index. If we want to use `inner`, we do this
  `pd.concat([s1,s4], axis=1, join="inner")`
* We can even specify the axes to be used on the other axes with `join_axes`.
  `pd.concat([s1,s2], axis=1, join_axes=[['a', 'c', 'b']])`
* When we concat them, we cannot tell which row belongs to which, we can do this:
  `pd.concat([s1,s2,s3],keys=['lala','haha','kaka'])`
    * In addition to use `keys` argument, you can just pass a dictionary to `concat`
      `pd.concat({'level1':df1, 'level2':df2}, axis=1)`
    * We can even give names to the `hier_index`:
      pd.concat({'level1':df1, 'level2':df2}, axis=1, names=['upper','lower'])
* If we want drop the index because it doesn't have any relevant info:
  `pd.concat([df1,df2], ignore_index=True)`
* Table 8-3 for reference

### 8.2.4 Combining Data with Overlap

* `overlap.py`
* Sometimes we want to update the `null` value in one `DataFrame` with
  the value in another `DataFrame`.
* `numpy` has `where` function, which is array oriented `if-else`
    * `np.where(pd.isnull(a), b, a)` will patch
* `combine_first` does the same thing
    * `np.array_equal(np.where(pd.isnull(a), b, a), a.combine_first(b).values)` will give `True`
