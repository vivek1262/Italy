from tkinter import *
from tkinter.ttk import *

root = Tk()

Label(root,text = "btn1").grid(row = 0,column =0,pady =10)
Label(root,text = "btn2").grid(row =1 ,column = 1,pady = 20)

Entry(root).grid(row = 0,column = 1,pady = 10)
Entry(root).grid(row = 1,column = 2,pady = 10)

Checkbutton(root,text ="btn").grid()

mainloop()