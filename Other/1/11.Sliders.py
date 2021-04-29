from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Sliders")

def get():
	print(f"We Credited You With {myslider2.get()} Rupee")
	tmsg.showinfo("Amount Credited", f"You Got\n{myslider2.get()} Rupee")


# myslider = Scale(root, from_=0, to=455)
# myslider.pack()

Label(root, text="How Many Money You Want").pack(pady=5)
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=25)
myslider2.set(50)
myslider2.pack(pady=5,padx=5)
Button(root, text="Get !!!", pady=5, padx=10, command=get).pack(pady=5)


root.mainloop()