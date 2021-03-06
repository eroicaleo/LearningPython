# This note is for my reference to all kinds of indexing method for Series and DataFrame

## Official document

* [Select and Indexing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)
* [MultiIndex / advanced indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-indexing-with-hierarchical-index)

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

* Select multiple rows consecutive and seperately with `.loc`

```python
In [27]: data.loc[:'Utah', 'two']
Out[27]:
Ohio        1
Colorado    5
Utah        9
Name: two, dtype: int64

In [28]: data.loc['Ohio':'Utah', 'two']
Out[28]:
Ohio        1
Colorado    5
Utah        9
Name: two, dtype: int64

In [29]: data.loc['Colorado':'Utah']
Out[29]:
          one  two  three  four
Colorado    4    5      6     7
Utah        8    9     10    11

In [30]: data.loc[['Ohio', 'Utah']]
Out[30]:
      one  two  three  four
Ohio    0    1      2     3
Utah    8    9     10    11
```

* Note the following 2 difference
    * The first: `data.iloc[:]` get the whole dataframe, then `[:3]` is slicing, so it's on the row
    * The second: use `iloc` to select row first, then column.

```
In [37]: data.iloc[:][:3]
Out[37]:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11

In [41]: data.iloc[:, :3]
Out[41]:
          one  two  three
Ohio        0    1      2
Colorado    4    5      6
Utah        8    9     10
New York   12   13     14
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

```python
frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     index=[['a','a','b','b'],[1,2,1,2]],
                     columns=[['Ohio','Ohio','Colorado'],
                              ['Green','Red','Green']])
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

Out[12]:
state      Ohio     Colorado
color     Green Red    Green
key1 key2
a    1        0   1        2
     2        3   4        5
b    1        6   7        8
     2        9  10       11
```

* Select outer level column

```python
In [13]: frame['Ohio']
Out[13]:
color      Green  Red
key1 key2
a    1         0    1
     2         3    4
b    1         6    7
     2         9   10
```

* Select outer level row

```python
In [17]: frame.loc['a']
Out[17]:
state  Ohio     Colorado
color Green Red    Green
key2
1         0   1        2
2         3   4        5
```

* Use `loc` to select row and column

```python
In [18]: frame.loc[['a','b'], 'Ohio']
Out[18]:
color      Green  Red
key1 key2
a    1         0    1
     2         3    4
b    1         6    7
     2         9   10
```

* Select inner column

```python
frame.loc[:, 'Ohio']['Green']

Out[35]:
key1  key2
a     1       0
      2       3
b     1       6
      2       9
Name: Green, dtype: int64
```

* select both `Green` columns, seems to be messy

```python
In [38]: frame.loc[:, [('Ohio', 'Green'), ('Colorado', 'Green')]]
Out[38]:
state      Ohio Colorado
color     Green    Green
key1 key2
a    1        0        2
     2        3        5
b    1        6        8
     2        9       11
```

* A more generic usage would be, it's inspired by the last example
  in this [section](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-indexing-with-hierarchical-index)

```python
In [56]: frame.loc[:, (list(frame.columns.droplevel(1).unique()), 'Green')]
Out[56]:
state      Ohio Colorado
color     Green    Green
key1 key2
a    1        0        2
     2        3        5
b    1        6        8
     2        9       11
```
