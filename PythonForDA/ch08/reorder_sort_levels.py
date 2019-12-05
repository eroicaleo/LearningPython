import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     index=[['a','a','b','b'],[1,2,1,2]],
                     columns=[['Ohio','Ohio','Colorado'],
                              ['Green','Red','Green']])

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

frame.swaplevel('key1', 'key2')
frame.swaplevel(0, 1, axis=0)
frame.swaplevel(0, 1, axis=1)
frame.swaplevel('state', 'color', axis=1)
frame.swaplevel(0, 1, axis=0).sort_index(level=0)
frame.swaplevel('state', 'color', axis=1).sort_index(level=0)
frame.swaplevel('state', 'color', axis=1).sort_index(level=0, axis=1)
frame.swaplevel(0, 1)
frame.sort_index(level=1)
frame.sort_index(level=0)
frame.sort_index(level=1, axis=1)
frame.sort_index(level=0, axis=1)
