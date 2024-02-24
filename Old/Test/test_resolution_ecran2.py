
# importing tkinter module
from tkinter import * 
from tkinter.ttk import *
 
# creating tkinter window
root = Tk()
 
# getting screen's height in pixels
height = root.winfo_screenheight()
 
# getting screen's width in pixels
width = root.winfo_screenwidth()
 
print("\n width x height = %d x %d (in pixels)\n" %(width, height))
# infinite loop
mainloop()