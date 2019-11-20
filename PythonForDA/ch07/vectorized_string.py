import numpy as np
import pandas as pd
import re

data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}

data = pd.Series(data)
data.shape
data[0]
data.index
data[-1]
data.isnull()
?pd.Series.map
data.str.contains('gmail')
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
data.str.findall(pattern, flags=re.IGNORECASE)
data.str.match(pattern, flags=re.IGNORECASE)
data.str.get(1)
data.str[0]
data.str[1]
data.str[:5]

