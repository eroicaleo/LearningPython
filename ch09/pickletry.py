#!/usr/local/bin/python3.3

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print(E)
F.close()
