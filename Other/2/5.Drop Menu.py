from tkinter import *

root= Tk()
root.title("Drop Down Menu")
root.geometry("500x400")

def show():
	Label(root, text="Your Selected " + choosed.get()).pack()
choosed = StringVar()
choosed.set("Choose")
drop = OptionMenu(root, choosed, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
drop.pack()
Button(root, text="Click Here", command=show).pack()


op=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
choosed_2 = StringVar()
choosed_2.set("Choose")
drop = OptionMenu(root, choosed_2, *op)
drop.pack()
Button(root, text="Click Here", command=show).pack()




root.mainloop()