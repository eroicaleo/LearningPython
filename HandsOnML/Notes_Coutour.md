
* This tutorial is based on Chapter 04
* See the [link](https://github.com/ageron/handson-ml/blob/master/04_training_linear_models.ipynb) here
  and search `bgd_path`

## Step1 generate `(x, y)` coordinates

```python
t1a, t1b, t2a, t2b = -1, 3, -1.5, 1.5

# These 2 generates points along each axis
t1s = np.linspace(t1a, t1b, 500)
t2s = np.linspace(t2a, t2b, 500)

# t1, t2 are both (500, 500) array
t1, t2 = np.meshgrid(t1s, t2s)

# combine them together
# it is (250000, 2) array
# from bottom left, to top right
T = np.c_[t1.ravel(), t2.ravel()]

```
