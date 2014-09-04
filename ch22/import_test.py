#!/usr/bin/env python3

import sys
import re
import time
import datetime
import os

for module in sorted(sys.modules):
    print("%-20s : %s" % (module, sys.modules[module]))

print('USER      : ', os.environ['USER'])
print('PWD       : ', os.environ['PWD'])
print('PYTHONPATH: ', os.environ.get('PYTHONPATH'))

print(sys.path)
