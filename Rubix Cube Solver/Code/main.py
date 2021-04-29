from tkinter import *
import cv2
import numpy as np
from PIL import ImageTk, Image
import kociemba as Cube
import tkinter.messagebox as tmsg
import os
import socket

root = Tk()
root.title("Rubix Cube Solver")
root.state("zoomed")
root.configure(bg='gray50')
root.iconbitmap("icon.ico")

val = {'r_h': 160, 'r_s': 170, 'o_h_min': 3, 'o_h_max': 10, 'y_h_min': 10, 'y_h_max': 25, 'g_h_min': 60, 'g_h_max': 90,
    'g_s': 100, 'g_v': 180, 'b_h_min': 25, 'b_h_max': 130, 'b_s': 70, 'w_h': 100, 'w_s': 10, 'w_v': 200, }

state = {'up': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'right': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'front': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'down': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'left': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'back': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ]}

sign_conv = {'green': 'F', 'white': 'U', 'blue': 'B', 'red': 'R', 'orange': 'L', 'yellow': 'D'}

color = {'red': (0, 0, 255), 'orange': (0, 140, 255), 'blue': (255, 0, 0), 'green': (0, 255, 0),
    'white': (255, 255, 255), 'yellow': (0, 255, 255)}

stickers = {'main': [[200, 120], [300, 120], [400, 120], [200, 220], [300, 220], [400, 220], [200, 320], [300, 320],
    [400, 320]], 'current': [[20, 20], [54, 20], [88, 20], [20, 54], [54, 54], [88, 54], [20, 88], [54, 88], [88, 88]],
    'preview': [[20, 130], [54, 130], [88, 130], [20, 164], [54, 164], [88, 164], [20, 198], [54, 198], [88, 198]],
    'left': [[50, 280], [94, 280], [138, 280], [50, 324], [94, 324], [138, 324], [50, 368], [94, 368], [138, 368]],
    'front': [[188, 280], [232, 280], [276, 280], [188, 324], [232, 324], [276, 324], [188, 368], [232, 368],
        [276, 368]],
    'right': [[326, 280], [370, 280], [414, 280], [326, 324], [370, 324], [414, 324], [326, 368], [370, 368],
        [414, 368]],
    'up': [[188, 128], [232, 128], [276, 128], [188, 172], [232, 172], [276, 172], [188, 216], [232, 216], [276, 216]],
    'down': [[188, 434], [232, 434], [276, 434], [188, 478], [232, 478], [276, 478], [188, 522], [232, 522],
        [276, 522]],
    'back': [[464, 280], [508, 280], [552, 280], [464, 324], [508, 324], [552, 324], [464, 368], [508, 368],
        [552, 368]], }

sidy = ['left', 'right', 'up', 'down', 'front', 'back']
for side in sidy:
    for i in range(len(stickers[side])):
        for j in range(len(stickers[side][i])):
            if j == 0:
                stickers[side][i][j] = stickers[side][i][j] - 30
            else:
                stickers[side][i][j] = stickers[side][i][j] - 100

font = cv2.FONT_HERSHEY_SIMPLEX
textPoints = {'up': [['U', 242, 202], ['W', (255, 255, 255), 260, 208]],
    'right': [['R', 380, 354], ['R', (0, 0, 255), 398, 360]], 'front': [['F', 242, 354], ['G', (0, 255, 0), 260, 360]],
    'down': [['D', 242, 508], ['Y', (0, 255, 255), 260, 514]],
    'left': [['L', 104, 354], ['O', (0, 169, 255), 122, 360]],
    'back': [['B', 518, 354], ['B', (255, 0, 0), 536, 360]], }

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

def calibrate(url):
    window = Toplevel()
    window.title("Set Cube Colours")
    window.state("zoomed")
    window.geometry("900x600")
    window.minsize(800, 600)
    window.maxsize(1366, 768)
    hsv_val = StringVar()

    def color_detect2(h, s, v):
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

    f0_c = Frame(window, bg = "black", borderwidth = 5, relief = SUNKEN)
    Label(f0_c, text = "Set Cube Colors", font = ("3Dumb", 22, "bold"), bg = "black", fg = "orange").pack()
    f0_c.pack(fill = "x")

    f1_c = Frame(window, padx = 5)
    input_frame_c = Label(f1_c, pady = 5, bg = "black", fg = "white")
    input_frame_c.pack(side = "left")
    f1_c.place(x = 700, y = 80)

    f2_c = Frame(window, bg = "orange", padx = 5)
    Label(f2_c, text = 'Min H For Orange', bg = 'orange', font = ('', 15)).pack(side = 'left', padx = 10)
    Entry(f2_c, textvariable = var1, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    Label(f2_c, text = 'Max H For Orange', bg = 'orange', font = ('', 15)).pack(side = 'left', padx = 30)
    Entry(f2_c, textvariable = var2, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f2_c.place(x = 10, y = 80, width = 650)

    f3_c = Frame(window, bg = "yellow", padx = 5)
    Label(f3_c, text = 'Min H For Yellow ', bg = 'yellow', font = ('', 15)).pack(side = 'left', padx = 10)
    Entry(f3_c, textvariable = var3, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    Label(f3_c, text = 'Max H For Yellow ', bg = 'yellow', font = ('', 15)).pack(side = 'left', padx = 30)
    Entry(f3_c, textvariable = var4, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f3_c.place(x = 10, y = 140, width = 650)

    f4_c = Frame(window, bg = "lightgreen", padx = 5)
    Label(f4_c, text = 'Min H For Green ', bg = "lightgreen", font = ('', 15)).pack(side = 'left', padx = 10)
    Entry(f4_c, textvariable = var5, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    Label(f4_c, text = 'Max H For Green  ', bg = "lightgreen", font = ('', 15)).pack(side = 'left', padx = 30)
    Entry(f4_c, textvariable = var6, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f4_c.place(x = 10, y = 200, width = 650)

    f5_c = Frame(window, bg = "lightgreen", padx = 5)
    Label(f5_c, text = 'S For Green       ', bg = "lightgreen", font = ('', 15)).pack(side = 'left', padx = 10)
    Entry(f5_c, textvariable = var7, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    Label(f5_c, text = 'V For Green         ', bg = "lightgreen", font = ('', 15)).pack(side = 'left', padx = 30)
    Entry(f5_c, textvariable = var8, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f5_c.place(x = 10, y = 260, width = 650)

    f6_c = Frame(window, bg = "tomato", padx = 5)
    Label(f6_c, text = 'H For Red          ', bg = "tomato", font = ('', 15)).pack(side = 'left', padx = 10)
    Entry(f6_c, textvariable = var9, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    Label(f6_c, text = 'S For Red            ', bg = "tomato", font = ('', 15)).pack(side = 'left', padx = 30)
    Entry(f6_c, textvariable = var10, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f6_c.place(x = 10, y = 320, width = 650)

    f7_c = Frame(window, bg = "antiqueWhite2", padx = 5)
    Label(f7_c, text = 'H For White        ', bg = "antiqueWhite2", font = ('', 15)).pack(side = 'left', padx = 10)
    Entry(f7_c, textvariable = var11, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    Label(f7_c, text = 'S For White         ', bg = "antiqueWhite2", font = ('', 15)).pack(side = 'left', padx = 30)
    Entry(f7_c, textvariable = var12, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f7_c.place(x = 10, y = 380, width = 650)

    f8_c = Frame(window, bg = "antiqueWhite2", padx = 5)
    Label(f8_c, text = 'V For White        ', bg = "antiqueWhite2", font = ('', 15)).pack(side = 'left', padx = 10)
    Entry(f8_c, textvariable = var13, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f8_c.place(x = 10, y = 440, width = 320)
    f9_c = Frame(window, bg = "skyblue", padx = 5)
    Label(f9_c, text = 'S For Blue         ', bg = "skyblue", font = ('', 15)).pack(side = 'left', padx = 30)
    Entry(f9_c, textvariable = var14, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f9_c.place(x = 340, y = 440, width = 320)

    f10_c = Frame(window, bg = "skyblue", padx = 5)
    Label(f10_c, text = 'Min H For Blue   ', bg = "skyblue", font = ('', 15)).pack(side = 'left', padx = 10)
    Entry(f10_c, textvariable = var15, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    Label(f10_c, text = 'Max H For Blue  ', bg = "skyblue", font = ('', 15)).pack(side = 'left', padx = 30)
    Entry(f10_c, textvariable = var16, width = 5).pack(pady = 5, padx = 5, side = 'left', ipady = 2)
    f10_c.place(x = 10, y = 500, width = 650)

    def exit_c():
        cap.release()
        window.destroy()

    Button(window, text = 'Default', font = ('', 15), command = default).place(x = 170, y = 540, height = 50, width = 100)
    Button(window, text = 'Update', font = ('', 15), command = update).place(x = 290, y = 540, height = 50, width = 100)
    Button(window, text = 'Exit', font = ('', 15), command = exit_c).place(x = 410, y = 540, height = 50, width = 100)
    Label(window, textvariable = hsv_val, font = ('', 15)).place(x = 10, y = 600)
    cap.open(url)
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        draw_stickers(img, stickers, 'main')
        hsv = []
        a = 0
        for i in range(9):
            hsv.append(frame[stickers['main'][i][1] + 10][stickers['main'][i][0] + 10])
        for x, y in stickers['current']:
            color_name = color_detect2(hsv[a][0], hsv[a][1], hsv[a][2])
            cv2.rectangle(img, (x, y), (x + 30, y + 30), color[color_name], -1)
            a += 1

        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_out = ImageTk.PhotoImage(Image.fromarray(img2))
        input_frame_c['image'] = img_out
        window.update()
    window.mainloop()

def open_help():
    help = Toplevel()
    help.title("Help")
    help.iconbitmap("icon.ico")
    help.geometry("500x500")
    help.minsize(500, 500)
    help.maxsize(1366, 768)
    t = ""
    with open("help.txt") as f:
        t = f.read()
    Scroll = Scrollbar(help)
    Scroll.pack(side=RIGHT, fill=Y)
    l1 = Text(help, yscrollcommand=Scroll.set, padx=5, pady=5, font=("Arial", "15"))
    l1.insert(1.0, t)
    l1.config(state="disabled")
    Scroll.config(command=l1.yview)
    l1.pack(expand=True, fill=BOTH)
    help.mainloop()

e1 =Entry()
e2 =Entry()
e3 =Entry()
e4 =Entry()
e5 =Entry()
def refresh():
    global e1, e2, e3, e4, e5
    address.set("")
    port.set("")
    user_var.set("")
    pass_var.set("")
    para.set("")
    for items in f3.winfo_children():
        items.destroy()
    cho = ch.get()
    if cho == "Webcam":
        Label(f3, text="Webcam ID : ", bg="pink", pady=5, padx=5).pack(side="left")
        e1 = Entry(f3, width=20, textvariable=address)
        e1.pack(pady=5, side="left")
    elif cho == "Stream":
        Label(f3, text="Enter The IP Address : ", pady=5, bg="pink", padx=5).pack(side="left")
        e1 = Entry(f3, width=20, textvariable=address)
        e1.pack(pady=5, side="left")
        Label(f3, text="Port : ", bg="pink", padx=5, pady=5).pack(side="left")
        e2 = Entry(f3, width=20, textvariable=port)
        e2.pack(pady=5, side="left")
        Label(f3, text="Any Parameter : ", bg="pink", padx=5, pady=5).pack(side="left")
        e3 = Entry(f3, width=20, textvariable=para)
        e3.pack(pady=5, side="left")
        Label(f3, text="Username : ", pady=5, bg="pink", padx=5).pack(side="left")
        e4 = Entry(f3, width=20, textvariable=user_var)
        e4.pack(pady=5, side="left")
        Label(f3, text="Password : ", bg="pink", padx=5, pady=5).pack(side="left")
        e5 = Entry(f3, width=20, textvariable=pass_var, show="*")
        e5.pack(pady=5, side="left")

def check_host():
    #  Checking For WebCam
    if ch.get() == "Webcam":
        try:
            cap.open(int(address.get()))
            if not cap.isOpened():
                tmsg.showerror("Error", "Can't Open WebCam\nMake Sure That WebCam Is Connected")
                return 0
        except ValueError:
            tmsg.showerror("Error", "Please Enter A Valid WebCam ID")
            return 0
    #  Checking For Streaming
    elif ch.get() == "Stream":
        host = True if os.system("ping -n 1 " + address.get()) is 0 else False  # Checking The IP return 1 is exist
        if address.get() == "":
            tmsg.showerror("Error", "Enter The IP Address")
            return 0
        elif host != 1:
            tmsg.showerror("Error", "Enter A Valid IP Address")
            return 0
        try:
            if port.get() == "":
                tmsg.showerror("Error", "Port Can't Be Blank")
                return 0
            elif 0 <= int(port.get()) <= 65535:
                a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                location = (address.get(), int(port.get()))
                result_of_check = a_socket.connect_ex(location)
                if result_of_check != 0:
                    tmsg.showerror("Error", "Port Is Not Open\nMake Sure Entered Port Is Right")
                    return 0
                a_socket.close()
            else:
                tmsg.showerror("Error", "Port Is Not Valid\nValid Range For Ports : 0-65535")
                return 0
        except ValueError:
            tmsg.showerror("Error", "Port Should Be A  Number")
            return 0
    else:
        tmsg.showwarning("Error", "Please Any Option")
        return 0
    return 1

def disconnect():
    global e1, e2, e3, e4, e5
    e1['state'] = 'normal'
    e2['state'] = 'normal'
    e3['state'] = 'normal'
    e4['state'] = 'normal'
    e5['state'] = 'normal'
    cap.release()
    cv2.destroyAllWindows()
def connect():
    global e1, e2, e3, e4, e5
    global url
    disconnect()
    cho = ch.get()
    if cho == "Webcam":
        url = int(address.get())
        if check_host():
            e1['state'] = 'disabled'
            cap.open(url)
            display_input(cap)
    elif cho == "Stream":
        if check_host():
            url = str(
                "http://" + user_var.get() + ":" + pass_var.get() + "@" + address.get() + ":" + port.get() + para.get())
            cap.open(url)
            if cap.isOpened():
                e1['state'] = 'disabled'
                e2['state'] = 'disabled'
                e3['state'] = 'disabled'
                e4['state'] = 'disabled'
                e5['state'] = 'disabled'
                display_input(cap)
            else:
                tmsg.showerror("Error", "Wrong Credentials Or Parameter")
    else:
        tmsg.showwarning("Error", "Please Choose One Option Before Connecting")

def exit_win():
    ans = tmsg.askyesno("Confirm Exit", "Are you sure you want to exit?")
    if ans == YES:
        disconnect()
        root.destroy()

check_state = []
solution = []
solved = False

def rotate(side):
    main = state[side]
    front = state['front']
    left = state['left']
    right = state['right']
    up = state['up']
    down = state['down']
    back = state['back']

    if side == 'front':
        left[2], left[5], left[8], up[6], up[7], up[8], right[0], right[3], right[6], down[0], down[1], down[2] = down[
            0], down[1], down[2], left[8], left[5], left[2], up[6], up[7], up[8], right[6], right[3], right[0]
    elif side == 'up':
        left[0], left[1], left[2], back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[
            2] = front[0], front[1], front[2], left[0], left[1], left[2], back[0], back[1], back[2], right[0], right[1],\
            right[2]
    elif side == 'down':
        left[6], left[7], left[8], back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[
            8] = back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[8], left[6], left[
            7], left[8]
    elif side == 'back':
        left[0], left[3], left[6], up[0], up[1], up[2], right[2], right[5], right[8], down[6], down[7], down[8] = up[2],\
            up[1], up[0], right[2], right[5], right[8], down[8], down[7], down[6], left[0], left[3], left[6]
    elif side == 'left':
        front[0], front[3], front[6], down[0], down[3], down[6], back[2], back[5], back[8], up[0], up[3], up[6] = up[0],\
            up[3], up[6], front[0], front[3], front[6], down[6], down[3], down[0], back[8], back[5], back[2]
    elif side == 'right':
        front[2], front[5], front[8], down[2], down[5], down[8], back[0], back[3], back[6], up[2], up[5], up[8] = down[
            2], down[5], down[8], back[6], back[3], back[0], up[8], up[5], up[2], front[2], front[5], front[8]

    main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[6], main[3], main[0], main[
        7], main[4], main[1], main[8], main[5], main[2]


def revrotate(side):
    main = state[side]
    front = state['front']
    left = state['left']
    right = state['right']
    up = state['up']
    down = state['down']
    back = state['back']

    if side == 'front':
        left[2], left[5], left[8], up[6], up[7], up[8], right[0], right[3], right[6], down[0], down[1], down[2] = up[8],\
            up[7], up[6], right[0], right[3], right[6], down[2], down[1], down[0], left[2], left[5], left[8]
    elif side == 'up':
        left[0], left[1], left[2], back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[
            2] = back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[2], left[0], left[
            1], left[2]
    elif side == 'down':
        left[6], left[7], left[8], back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[
            8] = front[6], front[7], front[8], left[6], left[7], left[8], back[6], back[7], back[8], right[6], right[7],\
            right[8]
    elif side == 'back':
        left[0], left[3], left[6], up[0], up[1], up[2], right[2], right[5], right[8], down[6], down[7], down[8] = down[
            6], down[7], down[8], left[6], left[3], left[0], up[0], up[1], up[2], right[8], right[5], right[2]
    elif side == 'left':
        front[0], front[3], front[6], down[0], down[3], down[6], back[2], back[5], back[8], up[0], up[3], up[6] = down[
            0], down[3], down[6], back[8], back[5], back[2], up[0], up[3], up[6], front[0], front[3], front[6]
    elif side == 'right':
        front[2], front[5], front[8], down[2], down[5], down[8], back[0], back[3], back[6], up[2], up[5], up[8] = up[2],\
            up[5], up[8], front[2], front[5], front[8], down[8], down[5], down[2], back[6], back[3], back[0]

    main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[2], main[5], main[8], main[
        1], main[4], main[7], main[0], main[3], main[6]

sol = True
def solve(state):
    raw = ''
    for i in state:
        for j in state[i]:
            raw += sign_conv[j]
    return Cube.solve(raw)


def draw_stickers(frame, stickers, name):
    for x, y in stickers[name]:
        cv2.rectangle(frame, (x, y), (x + 45, y + 45), (255, 255, 255), 2)


def fill_stickers(frame, stickers, sides):
    for side, colors in sides.items():
        num = 0
        for x, y in stickers[side]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), color[colors[num]], -1)
            num += 1

def texton_preview_stickers(frame, stickers):
    stick = ['front', 'back', 'left', 'right', 'up', 'down']
    for name in stick:
        for x, y in stickers[name]:
            sym, x1, y1 = textPoints[name][0][0], textPoints[name][0][1] - 30, textPoints[name][0][2] - 100
            cv2.putText(preview, sym, (x1, y1), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
            sym, col, x1, y1 = textPoints[name][1][0], textPoints[name][1][1], textPoints[name][1][2] - 30,\
                textPoints[name][1][3] - 100
            cv2.putText(preview, sym, (x1, y1), font, 0.5, col, 1, cv2.LINE_AA)

def color_detect(h, s, v):
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

i_len = 0
i_itr = 0
operation = []

def prev_sol(i_val, opr):
    i = opr[i_val]
    replace = {"F": [rotate, 'front'], "F2": [rotate, 'front', 'front'], "F'": [revrotate, 'front'],
        "U": [rotate, 'up'], "U2": [rotate, 'up', 'up'], "U'": [revrotate, 'up'], "L": [rotate, 'left'],
        "L2": [rotate, 'left', 'left'], "L'": [revrotate, 'left'], "R": [rotate, 'right'],
        "R2": [rotate, 'right', 'right'], "R'": [revrotate, 'right'], "D": [rotate, 'down'],
        "D2": [rotate, 'down', 'down'], "D'": [revrotate, 'down'], "B": [rotate, 'back'],
        "B2": [rotate, 'back', 'back'], "B'": [revrotate, 'back']}
    a = 0
    for j in range(len(replace[i]) - 1):
        replace[i][0](replace[i][j + 1])
    cv2.putText(preview, i, (700, a + 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
    fill_stickers(preview, stickers, state)
    solution.append(preview)
    img3 = cv2.cvtColor(preview, cv2.COLOR_BGR2RGB)
    img3 = ImageTk.PhotoImage(Image.fromarray(img3))
    pre_frame['image'] = img3

def display_input(cap):
    while True:
        hsv = []
        current_state = []
        ret, img = cap.read()
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = np.zeros(frame.shape, dtype = np.uint8)

        draw_stickers(img, stickers, 'main')
        fill_stickers(preview, stickers, state)
        texton_preview_stickers(preview, stickers)

        for i in range(9):
            hsv.append(frame[stickers['main'][i][1] + 10][stickers['main'][i][0] + 10])

        a = 0
        for x, y in stickers['current']:
            color_name = color_detect(hsv[a][0], hsv[a][1], hsv[a][2])
            cv2.rectangle(img, (x, y), (x + 30, y + 30), color[color_name], -1)
            a += 1
            current_state.append(color_name)

        def left(event):
            check_state.append('l')
            state['left'] = current_state

        def up(event):
            state['up'] = current_state
            check_state.append('u')

        def right(event):
            check_state.append('r')
            state['right'] = current_state

        def down(event):
            check_state.append('d')
            state['down'] = current_state

        def front(event):
            check_state.append('f')
            state['front'] = current_state

        def back(event):
            check_state.append('b')
            state['back'] = current_state

        def run(event):
            global sol
            if sol:
                if len(set(check_state)) == 6:
                    try:
                        solved = solve(state)
                        if solved:
                            global i_len
                            global operation
                            operation.extend(solved.split(' '))
                            i_len = len(operation)
                            sol = False
                    except:
                        tmsg.showerror("Scan Again",
                                       "Error in side detection, you may do not follow sequence or some color not detected well\nTry Again")

                else:
                    tmsg.showerror("Scaning Is Not Complete",
                                   f"All side are not scanned check other window for finding which left to be scanned?\nSide Left To Scan : {6 - len(set(check_state))}")

        def show_sol(event):
            global i_len
            global i_itr
            global operation
            if i_itr >= i_len and sol == False:
                tmsg.showinfo("Already Solved", "Cube Already Solved")
            else:
                a = ['Steps', ':']
                for x in range(i_itr):
                    a.extend(operation[x])
                    a.append('->')
                a.extend(operation[i_itr])
                ans.set(a)
                cv2.rectangle(preview, (670, 20), (750, 70), (0, 0, 0), -1)
                prev_sol(i_itr, operation)
                i_itr += 1

        def end(event):
            cap.release()
            cv2.destroyAllWindows()

        root.bind("<l>", left)
        root.bind("<L>", left)
        root.bind("<u>", up)
        root.bind("<U>", up)
        root.bind("<r>", right)
        root.bind("<R>", right)
        root.bind("<d>", down)
        root.bind("<D>", down)
        root.bind("<f>", front)
        root.bind("<F>", front)
        root.bind("<b>", back)
        root.bind("<B>", back)
        root.bind("<Return>", run)
        root.bind("<Right>", show_sol)
        root.bind("<Escape>", end)

        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img2 = img2[0:500, 0:500]
        img_out = ImageTk.PhotoImage(Image.fromarray(img2))
        input_frame['image'] = img_out
        img3 = cv2.cvtColor(preview, cv2.COLOR_BGR2RGB)
        img3 = ImageTk.PhotoImage(Image.fromarray(img3))
        pre_frame['image'] = img3
        root.update()

dim = (640, 480)
url = ''
cap = cv2.VideoCapture()
# cap.open(url)

f0 = Frame(root, bg = "black", borderwidth = 5, relief = SUNKEN)
Label(f0, text = "Rubix Cube Solver", font = ("Boneca de Pano", 30, "bold"), bg = "black", fg = "orange").pack()
f0.pack(fill = "x")

option_frame = Frame(root, pady=2, bg="plum1")
ch = StringVar()
ch.set("None")
Radiobutton(option_frame, text="Webcam", padx=14, variable=ch, value="Webcam", bg="plum1").pack(side="left")
Radiobutton(option_frame, text="Stream Webcam", padx=14, variable=ch, value="Stream", bg="plum1").pack(side="left")
option_frame.pack(anchor="w", fill="x")

address = StringVar()
port = StringVar()
para = StringVar()
user_var = StringVar()
pass_var = StringVar()
f3 = Frame(root, bg="pink", padx=10)
f3.pack(anchor="w", fill="x")

f4 = Frame(root, bg="palegreen", pady=5, padx=5)
Button(f4, text="Connect", command=connect).pack(side="left", padx=5)
Button(f4, text="Disconnect", command=disconnect).pack(side="left", padx=5)
Button(f4, text="Refresh", command=refresh).pack(side="left", padx=5)
Button(f4, text="Help", command=open_help).pack(side="left", padx=5)
Button(f4, text="Exit", command=exit_win).pack(side="left", padx=5)
Button(f4, text="Calibrate", command=(lambda : calibrate(url))).pack(side="left", padx=5)
f4.pack(fill="x")

ans = StringVar()
Label(root, textvariable = ans, font = ('', 17), bg='green').pack(fill='x')

f1 = Frame(root, padx = 5, bg = 'gray')
input_frame = Label(f1, pady = 5, bg='gray')
input_frame.pack(side = "left")
f1.place(x = 840, y = 210)

f2 = Frame(root, padx = 5, bg = 'gray')
pre_frame = Label(f2, pady = 5, bg = 'gray')
pre_frame.pack(side = 'left')
f2.place(x = 10, y = 210)

preview = np.zeros((483, 800, 3), np.uint8)
root.mainloop()
cap.release()
cv2.destroyAllWindows()
