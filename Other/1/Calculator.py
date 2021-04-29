from tkinter import *
root = Tk()
root.geometry("370x425")
root.title("Calculator By AK")

def click(event):
	global scvalue
	text = event.widget.cget(
		"text")
	print(text)
	if text == "=":
		if scvalue.get().isdigit():
			value = int(scvalue.get())
		else:
			try:
				value = eval(screen.get())
			except Exception as e:
				print(e)
				value = "Error"
		scvalue.set(value)
		screen.update()
	elif text == "C":
		scvalue.set("")
		screen.update()
	else :
		scvalue.set(scvalue.get() + text)
		screen.update()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill="x", ipadx=8, pady=10, padx=10)

f = Frame(root, bg="gray", padx=5)
b = Button(f, text="9", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="8", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="7", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="/", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="gray", padx=4)
b = Button(f, text="6", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="5", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="4", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="*", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="gray", padx=5)
b = Button(f, text="3", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="2", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="1", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="-", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="gray", padx=6)
b = Button(f, text="0", padx=12, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="C", padx=9, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="=", padx=11, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
b = Button(f, text="+", padx=9, pady=9, font="lucida 20 bold")
b.pack(side=LEFT, pady=5, padx=5)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()