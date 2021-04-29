from tkinter import *
root=Tk()
root.geometry("644x344")
root.minsize(500,300)
root.maxsize(1366,720)
root.title("Scroll Bar")

# For Connectinf scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)

# scrollbar = Scrollbar(root)
# scrollbar.pack(fill="y",side=RIGHT)
# lbx = Listbox(root, yscrollcommand = scrollbar.set)
# for i in range(1,101):
# 	lbx.insert(END, f"Item : {i}")
# lbx.pack(fill="both",padx=10,pady=10)
# scrollbar.config(command=lbx.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(fill="y",side=RIGHT)
text = Text(root, yscrollcommand = scrollbar.set, font="Lucida 15")
text.pack(fill="both")
scrollbar.config(command=text.yview)



root.mainloop()