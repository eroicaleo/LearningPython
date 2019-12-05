import numpy as np
import pandas as pd

frame = pd.DataFrame({'a': range(7),
                      'b': range(7,0,-1),
                      'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3],
                     })

frame
frame.set_index(['c'])
frame.set_index(['c', 'd'])
frame.set_index(['c', 'd'], drop=False)
frame.set_index(['d', 'd'], drop=False)
frame.set_index(['d', 'c'], drop=False)
frame.set_index(['c', 'd'])
frame.set_index(['d', 'c'])
frame.set_index(['d', 'c']).sort_index(level=0)
frame.set_index(['d', 'c']).sort_index(level=0).reset_index()

