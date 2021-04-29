from tkinter import *

def getvals():
	print(uservalue.get())
	print(passvalue.get())

root=Tk()
root.geometry("320x200")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Entry Widget & Grid Layout")

a = Label(root, text="Username : ")
b = Label(root, text="Password : ")
a.grid()
b.grid(row=1)

# Variable Classes In Tkinter
# BooleanVar, DoubleVar, Intvar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable = uservalue)
passentry = Entry(root,textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()