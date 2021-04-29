from tkinter import *
root=Tk()
root.geometry("320x200")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Frames")

f1 = Frame(root,bg="gray", borderwidth=6,relief=SUNKEN)
f1.pack(side="left",fill=Y,pady=50)

f2 = Frame(root, borderwidth=8, bg="gray", relief=GROOVE)
f2.pack(side=TOP, fill="x")

l1= Label(f1, text="Project Thinkter - Notepad")
l1.pack(pady=50)

l2= Label(f2, text="Title",bg="White",fg="red", font=(19))
l2.pack()

root.mainloop()