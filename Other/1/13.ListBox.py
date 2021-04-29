from tkinter import *
root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("List Box")

def add():
	global i
	lbx.insert(ACTIVE, f"{i}")
	i+=1
i=0	
lbx = Listbox(root)
lbx.pack();
lbx.insert(END, "First Item")
lbx.insert(END, "Second Item")
lbx.insert(END, "Third Item")

Button(text="Add Items", command=add).pack()

root.mainloop()