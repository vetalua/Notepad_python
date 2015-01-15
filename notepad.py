#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog
from tkMessageBox import *

'''
This program can be used as standart NOTEPAD in Windows
I create it for study how work with Tkinter and GUI in PYTHON
'''

############################################################################################################################################

def title_main_window(name = u'Noname'):
	'''Function make title of main window 	
	'''
	global file_name	# keep name of file, if it was saved to harddisc,  or Noname - if it was not saved
	global fix_change	# keep a number of nonsaved changed in file
	file_name = name
	fix_change = 0 		# it is 0 changes in new file or in saved file!
	root.title(u'  ' + name + u' - Notepad-Python')

def control_text_change(event):
	global fix_change
	fix_change = fix_change + 1
	#print fix_change  # only for test, must be comented in working version

def ask_save_changes():
	global fix_change
	answer = None
	if fix_change > 0:
		answer = askyesnocancel('Save changes?','Do you want to save your changes? If You select "No" - Chages will be lost!')
		if answer:
			save_func() # if canceling - return answer = None
	print answer
	return answer


##### Menu functions of main window ######

def new_hotkey(event): #it's for create new file with Ctrl+n maybe here must be @decorator
	global fix_change
	fix_change = fix_change - 1 # Ctrl + n = 1 presses!! not 2!
	#print fix_change
	new_func()
def new_func():
	answer = ask_save_changes()
	if answer == None:
		pass
	else:
		tx.delete('1.0', 'end')
		title_main_window()
	
def open_hotkey(event): #it's for opening with Ctrl+o maybe here must be @decorator
	global fix_change
	fix_change = fix_change - 1 # Ctrl + n = 1 presses!! not 2!
	print fix_change
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
	global fix_change
	if file_name == 'Noname': # if file is new, then saveas_func
		saveas_func()
	else:
		try:
			f= open(file_name, 'wt')
			f.write(tx.get('1.0', 'end'))
		finally:
			f.close()
	fix_change = 0

def saveas_func():
	fn = tkFileDialog.SaveAs(root, filetypes = [('*.py files', '.py')]).show()
	if fn == '':
		return
	if not fn.endswith(".py"):
		fn+=".py"
	try:
		open(fn, 'wt').write(tx.get('1.0', 'end'))
	finally:
		pass
		# close()
	title_main_window(fn) # for change title  of main window

def print_func():
	#TODO ALL!
	messege_notwork('"Print"')

def param_func():
	#TODO ALL!
	messege_notwork()

def exit_func():
	#TODO : This func must ask about saving before closing!!! 
	if askyesno('Exit', 'Do you want to quit?'):
		a = ask_save_changes()
		if a == None:
			pass
		else:
			root.destroy()
	pass


def about_func():
	showinfo('About program', 'This is FREE simple Notepad. \nIt was written with Python 2.7 and modul Tkinter by Tereshchenko Vitalii\n14.01.15')
	
def author_func():
	showinfo('About author', 'Author: Tereshchenko Vitalii \n e-mail: vetalt17@gmail.com \n Kharkiv 14.01.15')
	
def messege_notwork(not_worked_func = u'it'):
	''' All function wich not working now must query this function for output messege: Not work in current version
	'''
	showerror('Warning!', 'I am sorry \n but ' + not_worked_func + ' is not working in current version Notepad')
	
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

########## MAIN WINDOW ############

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


######## MENU ############

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
em.add_command(label = 'Copy         CTRL+C')
em.add_command(label = 'Paste        CTRL+V')
em.add_command(label = 'Cut          DEL')
em.add_command(label = 'Select all   CTRL+A')

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

######## HOT KEYS ###########

root.bind('<Control-n>',  new_hotkey)
root.bind('<Control-o>', open_hotkey)
root.bind('<Control-s>', save_hotkey)

# for count number changes in file after creating or saving:
root.bind('<KeyPress>', control_text_change) # Not best desicion, bicose control_text_change will be call out after pressing keys as: Ctrl, Shift, Esc...

root.mainloop() 