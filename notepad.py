#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog

'''
This program can be used as standart NOTEPAD in Windows
I create it for study how work with Tkinter and GUI in PYTHON
'''

############################################################################################################################################

def title_main_window(name = u' Noname'):
	'''Function make title of main window 	
	'''
	root.title(name + u' - Notepad-Python')


# Menu functions of main window 
def new_hotkey(event): #it's for create new file with Ctrl+n maybe here must be @decorator
	new_func()
def new_func():
# TODO: 1. call save_func if in old file was any not saving changes
#		2. clear text field for new file
	print 'Must clear textfild after saving/not saving'
	title_main_window()
	pass

def open_hotkey(event): #it's for opening with Ctrl+o maybe here must be @decorator
	open_func()
def open_func():
	fn = tkFileDialog.Open(root, filetypes = [('*.py files', '.py')]).show()
	if fn == '':
		return
	tx.delete('1.0', 'end') 
	tx.insert('1.0', open(fn, 'rt').read())
	title_main_window(fn) # for change title of main window
	
def save_hotkey(event): #it's for saving with Ctrl+s maybe here must be @decorator
	save_func()
def save_func():
	fn = tkFileDialog.SaveAs(root, filetypes = [('*.py files', '.py')]).show()
	if fn == '':
		return
	if not fn.endswith(".py"):
		fn+=".py"
	print fn
	try:
		open(fn, 'wt').write(tx.get('1.0', 'end'))
	finally:
		pass
		# close()
	title_main_window(fn) # for change title  of main window


def saveas_func():
	#TODO ALL!
	messege_notwork()

def print_func():
	#TODO ALL!
	messege_notwork()

def param_func():
	#TODO ALL!
	messege_notwork()

def exit_func():
	#TODO !
	print 'Save/withot save and exit saving/not saving'
	root.destroy()
	pass


def about_func():
	#TODO !
	win = Toplevel(root)
	win.title = 'About program'
	win.minsize(height = 75, width = 450)
	lab = Label (win,
	 text = u'This is FREE simple Notepad. \nIt was written with Python 2.7 and modul Tkinter by Tereshchenko Vitalii\n14.01.15')
	lab.pack(side = 'top')

def author_func():
	#TODO !
	win_auth = Toplevel(root)
	win_auth.title('About author')
	win_auth.minsize(height = 75, width = 450)
	lab = Label (win_auth, text = u'Author: Tereshchenko Vitalii \n e-mail: vetalt17@gmail.com \n Kharkiv 14.01.15')
	lab.pack(side = 'top')


def messege_notwork():
	''' All function wich not working now must query this function for output messege: Not work in current version
	'''
	win_auth = Toplevel(root)
	win_auth.title('Warning!')
	win_auth.minsize(height = 75, width = 450)
	lab = Label (win_auth, text = u'I am sorry \n but this function is not working in current version Notepad')
	lab.pack(side = 'top')
	

# TODO: create all function for menu
#		1. Create function select all, copy, paste, cut
#		2. select all, copy, paste, cut must work with mouse 

############################################################################################################################################

# size of window and widgets
min_height, min_width = 400, 500
max_height, max_width = 750, 1300
menu_height, menu_width = 50, 100
scroll_height, scroll_width = 20 , 20
tx_height, tx_width = 50 , 181

#############################################################################################################################################

########## Main window ############
root = Tk()

title_main_window()
#name = u'Noname'
#root.title(name + u' - Notepad-Python')
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


######## Menu ############

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
fm.add_command(label = 'Exit 	   Alt+F4', command = exit_func)

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
im.add_command(label = 'About Notepad-Python', command = about_func)
im.add_command(label = 'Author', command = author_func)
#im.add_command(label = 'Cut')
#im.add_command(label = 'Select all')

# Hot keys
root.bind('<Control-n>',  new_hotkey)
root.bind('<Control-o>', open_hotkey)
root.bind('<Control-s>', save_hotkey)
root.mainloop() 