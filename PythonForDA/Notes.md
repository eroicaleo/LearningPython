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
* page 91, table 4-2 to summarize
* `astype` to convert type
    * always create a new ndarray
