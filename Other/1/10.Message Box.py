from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Message Box")

def fun():
	print("Hello")

def help():
	print("I Will Help You")
	tmsg.showinfo("Help", "Bhagwan Sabki Maddad Karta Hai")

def rate():
	print("Rate Us")
	a = tmsg.askquestion("Was Your Experience", "You Used This GUI")
	print(a)
	if a == "no":
		msg = "Give Us Feedback"
	else:
		msg = "Thank You"
	tmsg.showinfo("Experience", msg)
def answerquestion():
	ans = tmsg.askretrycancel("Hello", "World")
	if ans:
		print("True")
	else:
		print("False")
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


m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Ask Question", command=answerquestion)
mainmenu.add_cascade(label="Submenu 3", menu=m3)

mainmenu.add_command(label="Help", command=help)
mainmenu.add_command(label="Rate Us", command=rate)
mainmenu.add_command(label="Exit", command=quit)

root.config(menu=mainmenu)

root.mainloop()