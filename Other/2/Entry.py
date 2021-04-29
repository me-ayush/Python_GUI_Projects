from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack(pady=15, fill="x")
e.insert(0, "Enter Your Name")

def click():
	l = Label(root, text = "Hello " + e.get())
	l.pack()

Button(root, text="Click Me", command=click).pack(pady=10)
root.mainloop()