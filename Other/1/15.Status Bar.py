from tkinter import *
root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Status Bar")

def upload():
	# statusvar.set("Busy...")
	# sbar.update()
	# import time
	# time.sleep(2)
	statusvar.set("Ready Now")

statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side="bottom",fill="x")

Button(root, text="Upload", command=upload).pack()

root.mainloop()