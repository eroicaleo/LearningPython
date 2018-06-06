#!/usr/bin/env python

from listinstance import ListInstance
from listinherited import ListInherited
from listtree import ListTree

Lister = ListTree

if __name__ == '__main__':
    print(ListInstance)
    print(Lister)
    Lister = ListInstance
    print(Lister)
