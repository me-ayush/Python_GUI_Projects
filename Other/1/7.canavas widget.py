from tkinter import *
root=Tk()
root.title("Canvas Widget")
root.minsize(800,400)
root.maxsize(1366,720)

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The Line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="black")

# To Create A Rectangle coordinates are(top_left, to bottom_right)
can_widget.create_rectangle(0, 0, 700, 300,fill="green")

# To Create A text coordinates(centre x,y)
can_widget.create_text(200, 200, text="python")

can_widget.create_oval(344, 233, 244, 355, fill="red")



# Rohan Das
# 1 year ago
# Harry = Canvas.create_image(x,y)
# #X and Y Coordinate Pe Image File Baith Jayega
# Rohan = canvas.create_bitmap(x,y)
# #x and y pe bitmap image ki place Ko define karta Hai! Hope Theek Se Samjhaya!
root.mainloop()