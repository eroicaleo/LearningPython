import numpy as np
import pandas as pd

val = 'a,b,  guido'
val.split(',')
pieces = [x.strip() for x in val.split(',')]
pieces
'::'.join(pieces)
'guido' in val
val.index(',')
val.find(':')
val.index(':')
val.count(',')
val.replace(',', '::')
val.replace(',', '')

