import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("250x250")
root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")

ttk.Label(tab1,text ="hit").grid(column = 0,row = 0,padx = 30,pady = 30)
ttk.Label(tab2,text ="hit me").grid(column = 0,row = 0,padx = 30,pady = 30)

root.mainloop()
