import numpy as np
import pandas as pd
import re

re.split('\s+', text)
regex = re.compile('\s+')
regex.split(text)
regex.findall(text)

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@gmail.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)

regex.findall(text)
m = regex.search(text)
m
text[m.start():m.end()]
regex.match(text)
print(regex.match(text))
print(regex.sub('REDACTED', text))
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match('wesm@bright.net')
m.groups()
regex.findall(text)
print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))
