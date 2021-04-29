from tkinter import *

def fun(event):
	print(f"You Clicked The Button At {event.x}, {event.y}")

root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Events In Tkinter")

widget = Button(root, text = "Click Me Please")
widget.pack()

widget.bind('<Button-1>', fun)
widget.bind('<Double-1>', quit)

root.mainloop()