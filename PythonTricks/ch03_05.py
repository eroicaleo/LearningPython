#!/usr/bin/env python

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))

print_vector(0, 1, 0)
tuple_vec = (1,0,1)
print_vector(tuple_vec[0],
             tuple_vec[1],
             tuple_vec[2])

list_vec = [1,0,1]
print_vector(*tuple_vec)
print_vector(*list_vec)
