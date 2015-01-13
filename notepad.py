#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

'''
This program can use as standart NOTEPAD in Windows
I create it for study how work with Tkinter and GUI
'''

############################################################################################################################################


############################################################################################################################################

# size of window and widgets
min_height, min_width = 400, 500
max_height, max_width = 750, 1300
menu_height, menu_width = 25, max_width
scroll_height, scroll_width = 20 , 20
tx_height, tx_width = 50 , 181

#############################################################################################################################################

root = Tk() # main window

#TODO 1: Name of window must consist of:  	1) "Noname" (if new document) or real name of file (if document allready save)
#											2) name of program - "Notepad-python"	
name = u'Noname'

root.title(name + u' - Notepad-Python')
root.minsize(height = min_height, width = min_width) # Min size of main window
root.maxsize(height = max_height, width = max_width)

fra_top = Frame(root, height = menu_height, width = menu_width, bg = 'darkgrey') # Frame for location of menu elements in top of main window
#fra_top.grid(row =0 , column = 0)

tx = Text(root, height = tx_height, width = tx_width, bg = 'white', font = "Verdana 8",	wrap = WORD) # textfield
tx.grid(row = 1, column = 0, sticky='nsew')

vscroll = Scrollbar(orient='vert', command=tx.yview) 
tx.configure(yscrollcommand=vscroll.set)
hscroll = Scrollbar(orient='hor', command=tx.xview)
tx.configure(xscrollcommand=hscroll.set)

print root.grid_size()

vscroll.grid(row=1, column = 1, sticky='ns')
hscroll.grid(row=2, column = 0, sticky='ew')

root.mainloop() 