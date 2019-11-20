# This note is for my reference to all kinds of indexing method for Series and DataFrame

## Official document

* [Select and Indexing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)

## Indexing in Regular Series

## Indexing in Regular DataFrame

* `ch05/indexing.py`
* Create a DataFrame

```
data = pd.DataFrame(np.arange(16).reshape(4,4), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
```

* Selete one column, and the type is `pd.Series`

```
data['two']

Ohio         1
Colorado     5
Utah         9
New York    13
Name: two, dtype: int64

type(data['two']) is pd.Series
True
```

* Another way: `data.two`

* Select multiple columns as follows. Select consecutive columns dosen't work like `pd.Series` object

```
data[['two', 'four']]

          two  four
Ohio        1     3
Colorado    5     7
Utah        9    11
New York   13    15

```

* Select multiple rows with slicing, this is a special case

```
data[:2]

          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7

# Note that data[2] will select a column called 2, but there is no such column.
# So there will be errors.
# Unless you add a new column

data[2] = [100,200,300,400]
date[2]

Ohio        100
Colorado    200
Utah        300
New York    400
Name: 2, dtype: int64
```

* Select multiple rows with boolean array

```
data[data['three'] > 5]

          one  two  three  four
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15

In [8]: data['three'] > 5
Out[8]:
Ohio        False
Colorado     True
Utah         True
New York     True
Name: three, dtype: bool
```

* Select row needs to use `.loc` and `.iloc`
    * `data.loc['Colorado', ['two', 'three']]`
    * `data.loc['Colorado'][['two', 'three']]`
    * `data.loc['Colorado']['two':'three']`
    * `data.loc['Colorado', 'two':'three']`

```
two      5
three    6
Name: Colorado, dtype: int64
```

## Indexing in Hierachical Series

```
data = pd.Series(np.random.randn(9), index=[['a','a','a','b','b','c','c','d','d'],[1,2,3,1,3,1,2,2,3]])
data

a  1    2.169219
   2   -0.330182
   3   -1.702174
b  1   -0.621665
   3    0.497261
c  1    0.679744
   2   -0.609199
d  2    0.103006
   3   -0.745304
```

* Select just one first level

```
data['b']

1   -0.621665
3    0.497261
dtype: float64
```

* Select consecutive first level

```
data['b':'c']

b  1   -0.621665
   3    0.497261
c  1    0.679744
   2   -0.609199
dtype: float64
```

* Select a couple of first level, has to group them in a list, `.loc` is optional

```
data.loc[['b', 'd']]

b  1   -0.621665
   3    0.497261
d  2    0.103006
   3   -0.745304
dtype: float64

data[['b', 'd']]

b  1   -0.621665
   3    0.497261
d  2    0.103006
   3   -0.745304
dtype: float64
```

* Select one second level

```
data.loc[:,2]

a   -0.330182
c   -0.609199
d    0.103006
```

* Select multiple second level, has to use a `list`

```
data.loc[:,[2,3]]

a  2   -0.330182
   3   -1.702174
b  3    0.497261
c  2   -0.609199
d  2    0.103006
   3   -0.745304
dtype: float64

# This doesn't work
# data.loc[:, [2:3]]
```

## Indexing in Hierachical DataFrame

