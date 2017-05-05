
# coding: utf-8

# In[1]:

import tkinter as tk


# In[2]:

prog_name = "Footprint Editor"


# In[17]:

root = tk.Tk()
root.geometry('350x350')
root.title(prog_name)


# In[18]:

new_file_icon = tk.PhotoImage(file='icons/new_file.gif')
open_file_icon = tk.PhotoImage(file='icons/open_file.gif')
save_file_icon = tk.PhotoImage(file='icons/save.gif')
cut_icon = tk.PhotoImage(file='icons/cut.gif')
copy_icon = tk.PhotoImage(file='icons/copy.gif')
paste_icon = tk.PhotoImage(file='icons/paste.gif')
undo_icon = tk.PhotoImage(file='icons/undo.gif')
redo_icon = tk.PhotoImage(file='icons/redo.gif')


# In[19]:

#cria o Widget Menu
top_menu = tk.Menu(root)


# In[20]:

#definições do item FILE
file_menu = tk.Menu(top_menu, tearoff=0)

file_menu.add_command(label="New", accelerator='Ctrl+N', compound='left' , image=new_file_icon ,  underline=0)
file_menu.add_command(label="Open", accelerator='Ctrl+O', compound='left' , image=open_file_icon ,  underline=0)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left' , image=save_file_icon ,  underline=0)
file_menu.add_command(label="Save as...", accelerator='Ctrl+Shift+S', compound='left',  underline=0)
file_menu.add_command(label="Exit", accelerator='Alt+F4', compound='left',  underline=0)

top_menu.add_cascade(label='File', menu=file_menu)

#definições do item Edit
edit_menu = tk.Menu(top_menu, tearoff=0)

edit_menu.add_command(label="Undo", accelerator='Ctrl+Z', compound='left')
edit_menu.add_command(label="Redo", accelerator='Ctrl+R', compound='left', underline = 0)
edit_menu.add_command(label="Undo", accelerator='Ctrl+Z', compound='left')
edit_menu.add_command(label="Cut", accelerator='Ctrl+X', compound='left')
edit_menu.add_command(label="Copy", accelerator='Ctrl+C', compound='left')
edit_menu.add_command(label="Paste", accelerator='Ctrl+V', compound='left')
edit_menu.add_command(label="Find", accelerator='Ctrl+F', compound='left', underline = 0)
edit_menu.add_command(label="Select All", accelerator='Ctrl+R', compound='left', underline = 0)

top_menu.add_cascade(label='Edit', menu=edit_menu)

#definições do item View
view_menu = tk.Menu(top_menu, tearoff=0)
top_menu.add_cascade(label='View', menu=view_menu)

#definições do item About
about_menu = tk.Menu(top_menu, tearoff=0)
top_menu.add_cascade(label='About', menu=about_menu)

root.config(menu=top_menu)
root.mainloop()


# In[9]:




# In[ ]:



