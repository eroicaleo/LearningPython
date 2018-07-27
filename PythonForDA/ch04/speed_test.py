# To be pasted in IPython

import numpy as np

my_arr = np.arange(1000000)

%time for _ in range(10): my_arr2 = my_arr * 2

my_list = list(range(1000000))
%time for _ in range(10): my_list2 = [x * 2 for x in my_list]
