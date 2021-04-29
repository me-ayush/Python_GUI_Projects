import cv2
import numpy as np
from tkinter import *
from PIL import ImageTk,Image
import datetime

def snap():
	image = Image.fromarray(img1)
	time = str(datetime.datetime.now().today()).replace(":","")+".jpg"
	image.save(time) 



root = Tk()
root.geometry("500x400")
root.configure(bg="black")
Label(root, text="Cam #1", font=("times new roman", 30, "bold"), bg="black", fg="red").pack()

f1 = LabelFrame(root, bg="red")
l1 = Label(f1, bg="red")
l1.pack(side="left")

l2 = Label(f1, bg="red")
l2.pack()

f1.pack()
cap = cv2.VideoCapture(0)
f3 = Frame(root)
Button(f3, text="Take A Snap", font=("times new roman", 30, "bold"), bg="black", fg="red", command=snap).pack(fill="x", expand="Y")
f3.pack()
while True:
	img = cap.read()[1]
	img = cv2.flip(img,1)
	img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img = ImageTk.PhotoImage(Image.fromarray(img1))
	l1['image'] = img
	l2['image'] = img
	root.update()

cap.release()