from tkinter import *
root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Grid Layouts 2")

def getvals():
	print("Form Submitted")
	with open("records.txt","a") as f:
		f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emervalue.get(), payvalue.get(), foodserviceval.get()}\n")

# Heading
Label(root, text="Welcome To ABC Travels", font="comicsansms 20 bold", pady=15).grid(row=0,column=3)

# Text For Our Form
name = Label(root, text="Name : ")
phone = Label(root, text="Phone : ")
gender = Label(root, text="Gender : ")
emer = Label(root, text="Emergency Number : ")
pay = Label(root, text="Payment Mode : ")
# Packing Texts For Form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emer.grid(row=4,column=2)
pay.grid(row=5,column=2)

# Variables For Storing Entry
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emervalue = StringVar()
payvalue = StringVar()
foodserviceval = IntVar()
# Entries For Our Form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emerentry = Entry(root, textvariable=emervalue)
payentery = Entry(root, textvariable=payvalue)

# Packing The Entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emerentry.grid(row=4,column=3)
payentery.grid(row=5,column=3)

# Checkbox
foodservice = Checkbutton(text = "Want To PreBook Your Maels", variable = foodserviceval)
foodservice.grid(row=6,column=3)

# Button & packing it and assigninisg it a command
Button(text="Submit", command=getvals).grid(row=7,column=2)

root.mainloop()