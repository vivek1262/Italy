from tkinter import *
from tkinter.ttk import *

master = Tk()
master.geometry('250x200')

Lower = Label(master,text='Lower_left')

Lower.place(relx=0.0,rely=1.0,anchor='sw')
master.mainloop()