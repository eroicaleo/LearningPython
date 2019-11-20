import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(1000, 4))
data.describe()
data.head()
col = data[2]
col[np.abs(col) > 3]
np.abs(data) > 3
(np.abs(data) > 3).any(1)
data[(np.abs(data) > 3).any(1)]
data.describe()
data[np.abs(data) > 3] = np.sign(data) * 3.0
data.describe()
np.sign(data)
np.sign(data).head()
