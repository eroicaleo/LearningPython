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
