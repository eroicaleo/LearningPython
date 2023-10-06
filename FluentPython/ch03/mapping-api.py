import abc

'''
>>> my_dict = {}
>>> isinstance(my_dict, abc.Mapping)
True
>>> isinstance(my_dict, abc.MutableMapping)
True
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
