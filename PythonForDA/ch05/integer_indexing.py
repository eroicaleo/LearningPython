import numpy as np
import pandas as pd
ser = pd.Series(np.arange(3.))
ser
ser[-1]
ser.iloc[-1]
ser2 = pd.Series(np.arange(3.), index=list('abc'))
ser2[-1]
ser.iloc[:1]
ser.loc[:1]
