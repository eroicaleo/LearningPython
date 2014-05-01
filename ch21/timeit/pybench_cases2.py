#!/usr/bin/env python3

import sys, pybench

pythons = [
        (1, '/usr/bin/python3'),
        (0, '/usr/bin/python2')
        ]

stmts = [
        # Use function calls: map wins
        (0, 0, "[ord(x) for x in 'spam' * 2500]"),
        (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
        (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
        (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
        # Set and dicts
        (0, 0, "{x ** 2 for x in range(1000)}"),
        (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
        (0, 0, "{x: x ** 2 for x in range(1000)}"),
        (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),
        # Pathological: 300k digits
        (1, 1, "len(str(2**1000000))")
        ]

tracecmd = '-t' in sys.argv

pythons = pythons if '-a' in sys.argv else None

pybench.runner(stmts, pythons, tracecmd)
