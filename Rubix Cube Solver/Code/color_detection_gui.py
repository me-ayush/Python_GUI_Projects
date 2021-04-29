from tkinter import *
from PIL import ImageTk, Image
import cv2
window = Tk()
window.title("Set Cube Colours")
window.state("zoomed")
window.geometry("900x600")
window.minsize(800, 600)
window.maxsize(1366, 768)

color = {'red': (0, 0, 255), 'orange': (0, 140, 255), 'blue': (255, 0, 0), 'green': (0, 255, 0),
    'white': (255, 255, 255), 'yellow': (0, 255, 255)}
stickers = {'main': [[200, 120], [300, 120], [400, 120], [200, 220], [300, 220], [400, 220], [200, 320], [300, 320],
    [400, 320]], 'current': [[20, 20], [54, 20], [88, 20], [20, 54], [54, 54], [88, 54], [20, 88], [54, 88], [88, 88]]}

def draw_stickers(frame, stickers, name):
    for x, y in stickers[name]:
        cv2.rectangle(frame, (x, y), (x + 45, y + 45), (255, 255, 255), 2)

val = {'r_h': 160, 'r_s': 170, 'o_h_min': 3, 'o_h_max': 10, 'y_h_min': 10, 'y_h_max': 25, 'g_h_min': 60, 'g_h_max': 90,
    'g_s': 100, 'g_v': 180, 'b_h_min': 25, 'b_h_max': 130, 'b_s': 70, 'w_h': 100, 'w_s': 10, 'w_v': 200, }

var1 = IntVar(value = val['o_h_min'])
var2 = IntVar(value = val['o_h_max'])
var3 = IntVar(value = val['y_h_min'])
var4 = IntVar(value = val['y_h_max'])
var5 = IntVar(value = val['g_h_min'])
var6 = IntVar(value = val['g_h_max'])
var7 = IntVar(value = val['g_s'])
var8 = IntVar(value = val['g_v'])
var9 = IntVar(value = val['r_h'])
var10 = IntVar(value = val['r_s'])
var11 = IntVar(value = val['w_h'])
var12 = IntVar(value = val['w_s'])
var13 = IntVar(value = val['w_v'])
var14 = IntVar(value = val['b_s'])
var15 = IntVar(value = val['b_h_min'])
var16 = IntVar(value = val['b_h_max'])

def default():
    val['o_h_min'] = 3
    val['o_h_max'] = 10
    val['y_h_min'] = 10
    val['y_h_max'] = 25
    val['g_h_min'] = 60
    val['g_h_max'] = 90
    val['g_s'] = 100
    val['g_v'] = 180
    val['r_h'] = 160
    val['r_s'] = 170
    val['w_h'] = 100
    val['w_s'] = 10
    val['w_v'] = 200
    val['b_s'] = 70
    val['b_h_min'] = 25
    val['b_h_max'] = 130

def update():
    val['o_h_min'] = var1.get()
    val['o_h_max'] = var2.get()
    val['y_h_min'] = var3.get()
    val['y_h_max'] = var4.get()
    val['g_h_min'] = var5.get()
    val['g_h_max'] = var6.get()
    val['g_s'] = var7.get()
    val['g_v'] = var8.get()
    val['r_h'] = var9.get()
    val['r_s'] = var10.get()
    val['w_h'] = var11.get()
    val['w_s'] = var12.get()
    val['w_v'] = var13.get()
    val['b_s'] = var14.get()
    val['b_h_min'] = var15.get()
    val['b_h_max'] = var16.get()

hsv_val = StringVar()
def color_detect(h, s, v):
    a = f"Current Fetching Values : H = {h} S = {s} V = {v}"
    hsv_val.set(a)
    if h > val['r_h'] and s > val['r_s']:
        return 'red'
    elif val['o_h_max'] > h >= val['o_h_min']:
        return 'orange'
    elif val['y_h_max'] >= h > val['y_h_min']:
        return 'yellow'
    elif val['g_h_min'] <= h <= val['g_h_max'] and s > val['g_s'] and v < val['g_v']:
        return 'green'
    elif val['b_h_min'] <= h <= val['b_h_max'] and s > val['b_s']:
        return 'blue'
    elif h <= val['w_h'] and s < val['w_s'] and v < val['w_v']:
        return 'white'
    return 'white'

f0 = Frame(window, bg = "black", borderwidth = 5, relief = SUNKEN)
Label(f0, text = "Set Cube Colors", font = ("3Dumb", 22, "bold"), bg = "black", fg = "orange").pack()
f0.pack(fill = "x")

f1 = Frame(window, padx = 5)
input_frame = Label(f1, pady = 5, bg = "black", fg = "white")
input_frame.pack(side = "left")
f1.place(x = 700, y = 80)

f2 = Frame(window, bg = "orange", padx = 5)
Label(f2, text = 'Min H For Orange', bg = 'orange', font = ('', 15)).pack(side = 'left', padx = 10)
Entry(f2, textvariable = var1, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
Label(f2, text = 'Max H For Orange', bg = 'orange', font = ('', 15)).pack(side = 'left', padx = 30)
Entry(f2, textvariable = var2, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f2.place(x = 10, y = 80, width = 650)

f3 = Frame(window, bg = "yellow", padx = 5)
Label(f3, text = 'Min H For Yellow ', bg = 'yellow', font = ('', 15)).pack(side = 'left', padx = 10)
Entry(f3, textvariable = var3, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
Label(f3, text = 'Max H For Yellow ', bg = 'yellow', font = ('', 15)).pack(side = 'left', padx = 30)
Entry(f3, textvariable = var4, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f3.place(x = 10, y = 140, width = 650)

f4 = Frame(window, bg = "lightgreen", padx = 5)
Label(f4, text = 'Min H For Green ', bg = "lightgreen", font = ('', 15)).pack(side = 'left', padx = 10)
Entry(f4, textvariable = var5, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
Label(f4, text = 'Max H For Green  ', bg = "lightgreen", font = ('', 15)).pack(side = 'left', padx = 30)
Entry(f4, textvariable = var6, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f4.place(x = 10, y = 200, width = 650)

f5 = Frame(window, bg = "lightgreen", padx = 5)
Label(f5, text = 'S For Green       ', bg = "lightgreen", font = ('', 15)).pack(side = 'left', padx = 10)
Entry(f5, textvariable = var7, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
Label(f5, text = 'V For Green         ', bg = "lightgreen", font = ('', 15)).pack(side = 'left', padx = 30)
Entry(f5, textvariable = var8, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f5.place(x = 10, y = 260, width = 650)

f6 = Frame(window, bg = "tomato", padx = 5)
Label(f6, text = 'H For Red          ', bg = "tomato", font = ('', 15)).pack(side = 'left', padx = 10)
Entry(f6, textvariable = var9, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
Label(f6, text = 'S For Red            ', bg = "tomato", font = ('', 15)).pack(side = 'left', padx = 30)
Entry(f6, textvariable = var10, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f6.place(x = 10, y = 320, width = 650)

f7 = Frame(window, bg = "antiqueWhite2", padx = 5)
Label(f7, text = 'H For White        ', bg = "antiqueWhite2", font = ('', 15)).pack(side = 'left', padx = 10)
Entry(f7, textvariable = var11, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
Label(f7, text = 'S For White         ', bg = "antiqueWhite2", font = ('', 15)).pack(side = 'left', padx = 30)
Entry(f7, textvariable = var12, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f7.place(x = 10, y = 380, width = 650)

f8 = Frame(window, bg = "antiqueWhite2", padx = 5)
Label(f8, text = 'V For White        ', bg = "antiqueWhite2", font = ('', 15)).pack(side = 'left', padx = 10)
Entry(f8, textvariable = var13, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f8.place(x = 10, y = 440, width = 320)
f9 = Frame(window, bg = "skyblue", padx = 5)
Label(f9, text = 'S For Blue         ', bg = "skyblue", font = ('', 15)).pack(side = 'left', padx = 30)
Entry(f9, textvariable = var14, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f9.place(x = 340, y = 440, width = 320)

f10 = Frame(window, bg = "skyblue", padx = 5)
Label(f10, text = 'Min H For Blue   ', bg = "skyblue", font = ('', 15)).pack(side = 'left', padx = 10)
Entry(f10, textvariable = var15, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
Label(f10, text = 'Max H For Blue  ', bg = "skyblue", font = ('', 15)).pack(side = 'left', padx = 30)
Entry(f10, textvariable = var16, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
f10.place(x = 10, y = 500, width = 650)

Button(window, text = 'Default', font = ('', 15), command = default).place(x = 190, y = 540, height=50, width = 100)
Button(window, text = 'Update', font = ('', 15), command = update).place(x = 310, y = 540, height=50, width = 100)
Label(window, textvariable = hsv_val, font = ('', 15)).place(x=10, y = 600)



dim = (640, 480)
cap = cv2.VideoCapture()
url = "http://192.168.43.209:8080/video"
cap.open(url)
while True:

    ret, img = cap.read()
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    draw_stickers(img, stickers, 'main')
    hsv = []
    a = 0
    for i in range(9):
        hsv.append(frame[stickers['main'][i][1] + 10][stickers['main'][i][0] + 10])
    for x, y in stickers['current']:
        color_name = color_detect(hsv[a][0], hsv[a][1], hsv[a][2])
        cv2.rectangle(img, (x, y), (x + 30, y + 30), color[color_name], -1)
        a += 1

    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_out = ImageTk.PhotoImage(Image.fromarray(img2))
    input_frame['image'] = img_out
    window.update()

window.mainloop()
