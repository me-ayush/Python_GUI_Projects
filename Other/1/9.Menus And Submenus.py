from tkinter import *
root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Menus And Submenus")

def fun():
	print("Hello World")

# Use These To Create A Non-DropDown Menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=fun)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

mainmenu = Menu(root)
# mymenu = add_command(label="Exit", quit)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New", command=fun)
m1.add_command(label="Save", command=fun)
m1.add_separator()
m1.add_command(label="Save As", command=fun)
m1.add_command(label="Print", command=fun)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="New", command=fun)
m2.add_command(label="Save", command=fun)
m2.add_separator()
m2.add_command(label="Save As", command=fun)
m2.add_command(label="Print", command=fun)
mainmenu.add_cascade(label="File 2", menu=m2)

mainmenu.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)


root.mainloop()