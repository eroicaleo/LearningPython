#!/usr/local/bin/python3.3

import sys
from tkinter import Button, mainloop # Tkinter in 2.X
x = Button(
        text='Press me',
        command=(lambda:sys.stdout.write('Spam\n'))) # 3.X: print()
x.pack()
mainloop()
