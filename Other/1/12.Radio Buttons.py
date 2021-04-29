from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Radio Buttons")


def order():
	tmsg.showinfo("Order Recived", f"We Have Recived Your Order For {var.get()}.\nThanks For Ordering")
# var = IntVar()
# var.ser(1)
var = StringVar()
var.set("radio")
Label(root, text = "What Would You Like To Eat...?", justify=LEFT, padx=14,font="Lucida 19 bold").pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")
Button(text="Order Now", command=order).pack()



root.mainloop()