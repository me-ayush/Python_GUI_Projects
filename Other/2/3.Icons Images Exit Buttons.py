from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Icons")
root.iconbitmap("1.ico")

# my_img = ImageTk.PhotoImage(Image.open("img.jpg"))
# Label(image=my_img, width=500, height=500).pack()

image = Image.open("img.jpg")
image = image.resize((450, 350), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
Label(root,image = my_img).pack()

button_quit = Button(root, text="Exit Program", command=quit)
button_quit.pack()


root.mainloop()