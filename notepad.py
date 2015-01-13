#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

'''
This program can use as standart NOTEPAD in Windows
I create it for study how work with Tkinter and GUI
'''

############################################################################################################################################

# Functions of menu

def new_func():
	#TODO ALL!
	print 'Must clear textfild after saving/not saving'
	pass

def open_func():
	#TODO ALL!
	print 'Must show tree of files for choose, and open file after choosing'
	pass

def save_func():
	#TODO ALL!
	print 'Must clear textfild after saving/not saving'
	pass

def saveas_func():
	#TODO ALL!
	print 'Must clear textfild after saving/not saving'
	pass

def print_func():
	#TODO ALL!
	print 'Must clear textfild after saving/not saving'
	pass

def param_func():
	#TODO ALL!
	print 'Must clear textfild after saving/not saving'
	pass

def exit_func():
	#TODO !
	print 'Save/withot save and exit saving/not saving'
	root.destroy()
	pass

# TODO: create all function for menu

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

#fra_top = Frame(root, height = menu_height, width = menu_width, bg = 'darkgrey') # Frame for location of menu elements in top of main window
#fra_top.grid(row =0 , column = 0)
#fra_top.pack(side = 'top')
fra_bot = Frame(root, height = max_height, width = max_width, bg = 'grey') # Frame for location of textfield in the bottom of main window
fra_bot.pack(side = 'top')

tx = Text(fra_bot, height = tx_height, width = tx_width, bg = 'white', font = "Verdana 8",	wrap = WORD) # textfield
tx.grid(row = 1, column = 0, sticky='nsew')

vscroll = Scrollbar(fra_bot, orient='vert', command=tx.yview) 
tx.configure(yscrollcommand=vscroll.set)
vscroll.grid(row=1, column = 1, sticky='ns')

hscroll = Scrollbar(fra_bot, orient='hor', command=tx.xview)  # to be or not to be?!
tx.configure(xscrollcommand=hscroll.set)
hscroll.grid(row=2, column = 0, sticky='ew')

# Menu
m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label = 'File', menu = fm)
fm.add_command(label = 'New        CTRL+N', command = new_func)
fm.add_command(label = 'Open       CTRL+O', command = open_func)
fm.add_command(label = 'Save       CTRL+S', command = save_func)
fm.add_command(label = 'Save as...', command = saveas_func)
fm.add_command(label = 'Parameters...', command = param_func)
fm.add_command(label = 'Print...', command = print_func)
fm.add_command(label = 'Exit', command = exit_func)

em = Menu(m)
m.add_cascade(label = 'Edit', menu = em)
em.add_command(label = 'Copy')
em.add_command(label = 'Paste')
em.add_command(label = 'Cut')
em.add_command(label = 'Select all')

fom = Menu(m)
m.add_cascade(label = 'Format', menu = fom)
sfom = Menu(fom)
fom.add_cascade(label = 'Text size', menu = sfom) # put in menu choose of size
sfom.add_command(label='6')
sfom.add_command(label='8')
sfom.add_command(label='10')
sfom.add_command(label='12')
sfom.add_command(label='14')

fom.add_command(label = 'Scale')
#fom.add_command(label = '?')
#fom.add_command(label = '?')

vm = Menu(m)
m.add_cascade(label = 'View', menu = vm)
vm.add_command(label = '@@@')
vm.add_command(label = '@@@@')
vm.add_command(label = '@@@@@')
vm.add_command(label = '@@@@@@')

im = Menu(m)
m.add_cascade(label = 'Info', menu = im)
im.add_command(label = 'About Notepad-Python')
im.add_command(label = 'Author')
#im.add_command(label = 'Cut')
#im.add_command(label = 'Select all')

root.mainloop() 