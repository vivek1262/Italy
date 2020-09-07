from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('200x200')
frame = Frame(root)

frame.pack()

btn = Button(root,text = "Buttin 1",command = root.destroy)
btn.pack()
btn2 = Button(root,text = "Button 2",command = btn.destroy)
btn2.pack(pady = 10)
btn3 = Button(root,text = "Button 3",command = btn2.destroy)
btn3.pack(pady = 10)
messagebox.showinfo('info',"press these buttons")
root.mainloop()