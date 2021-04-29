from tkinter import *

def hello():
	print("Hello World")

root=Tk()
root.geometry("320x200")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Buttons")

frame_1 = Frame(root,borderwidth=6,bg="grey",relief=GROOVE)
frame_1.pack(side=LEFT,anchor="nw")

b1 = Button(frame_1,fg="red",text="Click Here 1", command=hello)
b1.pack(side=LEFT)

b2 = Button(frame_1,fg="red",text="Click Here 2")
b2.pack()

b3 = Button(frame_1,fg="red",text="Click Here 3")
b3.pack()

b4 = Button(frame_1,fg="red",text="Click Here 4")
b4.pack()

root.mainloop()