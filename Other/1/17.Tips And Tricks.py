from tkinter import *
root = Tk()
root.geometry("644x344")
root.title("Tips And Tricks")
root.wm_iconbitmap("1.ico")	#For Icon
root.configure(bg="gray") #For Updation In Your GUI

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f" Width : {width} Height : {height}")

Button(text="Close", command=root.destroy).pack()


root.mainloop()