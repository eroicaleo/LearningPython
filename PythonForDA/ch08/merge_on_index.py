#!/usr/bin/env python3

import numpy as np
import pandas as pd

left1 = pd.DataFrame({'key': list('abaabc'),
                     'value': range(6)})

right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.0)})


righth = pd.DataFrame({})

righth = pd.DataFrame(np.arange(12).reshape(6,2),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'], [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])

left2 = pd.DataFrame([[1.,2.], [3.,4.], [5.,6.]], index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])

right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13., 14.]], index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])

another = pd.DataFrame([[7.,8.], [9., 10,], [11.,12.],[13.,14.]], index=['a','c','e','f'], columns=['New York', 'Oregon'])

left1 = pd.DataFrame({'key': list('abaabc'),
                     'value': range(6)})
left1
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
right1
pd.merge(left=left1, right=right1, left_on='key', right_index=True)
pd.merge(left=left1, right=right1, left_on='key', right_index=True, how='outer')
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': range(5)})
lefth
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': range(5.0)})
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.0)})
lefth
righth = pd.DataFrame(np.arange(12).reshape(6,2),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'], [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
righth
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')
left2 = pd.DataFrame([[1.,2.], [3.,4.], [5.,6.]], index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])
left2
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13., 14.]], index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
right2
pd.merge(left2, right2, how='outer')
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
left2.join(right2, how='outer')
left1
right1
left1.join(right1)
left1.join(right1, on='key')
another = pd.DataFrame([[7.,8.], [9., 10,], [11.,12.],[13.,14.]], index=['a','c','e','f'], columns=['New York', 'Oregon'])
left2.join([right2, another])
left2.join([right2, another], how='outer')
