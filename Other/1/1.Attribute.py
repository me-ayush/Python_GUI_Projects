from tkinter import *
root=Tk()
root.title("GUI Application")
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)

# Important Label Option
# text = add text
# bg = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# font=("Bradley Hand ITC", 19,"bold")
# font="Cooper 19 bold"
# relief = border styling = SUNKEN , RAISED, GROOVE, RIDGE
text_1=Label(text = '''Hello World''', bg="red", fg="yellow", padx=20, pady=10, font=("Bradley Hand ITC", 19,"bold"), borderwidth=30,relief=RIDGE)

# important Pack Option
# anchor =n,s,w,e,nw,se,sw...
# side = top(default), bottom, left, right
# fill = x/Y
text_1.pack(side=LEFT,anchor="nw",fill="y",padx=20,pady=20)


root.mainloop()