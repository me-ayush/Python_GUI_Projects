from tkinter import *

root =Tk()
root.geometry("500x400")
root.title("First Window")

def open():
	top = Toplevel()
	top.geometry("500x400")
	top.title("Second Window")
	lbl = Label(top, text="This Is Second Window").pack()	
	Button(top, text="Exit This Window", command=top.destroy).pack()
	Button(top, text="Exit", command=root.destroy).pack()

Button(root, text="Click Here To Open Second Window", command=open).pack()


root.mainloop()