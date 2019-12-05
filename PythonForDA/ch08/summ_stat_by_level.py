import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     index=[['a','a','b','b'],[1,2,1,2]],
                     columns=[['Ohio','Ohio','Colorado'],
                              ['Green','Red','Green']])

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

frame.sum(level='key2')
frame.sum(level=0)
frame.sum(level=1)
frame.sum(level='color', axis=1)
frame.sum(level=0, axis=1)
