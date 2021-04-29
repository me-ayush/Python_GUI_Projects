from tkinter import *

class GUI(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("600x350")
		self.title("Classes And Objects")

	def status(self):
		self.var = StringVar()
		self.var.set("Ready")
		self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
		self.statusbar.pack(side="bottom", fill="x")

if __name__ == '__main__':
	window = GUI()
	window.status()
	window.mainloop()