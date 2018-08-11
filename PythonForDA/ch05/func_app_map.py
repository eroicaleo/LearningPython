import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.rand(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
np.abs(frame)
f = lambda x: x.max() - x.min()
frame.apply(f)
frame.apply(f, axis='columns')
frame.sum()
frame.mean()
def f(x):
    return pd.Series([x.max(), x.min()], index=['max', 'min'])
frame.apply(f)
frame.apply(f, axis='columns')
format = lambda x: '%.2f' % x
frame.applymap(format)
frame
frame['e'].map(format)
