import pytesseract
import tkinter as tk
import cv2
import numpy as np
import urllib.request
import keyboard as key
from PIL import Image

a = Image.open("a.png")
b = Image.open("b.png")
c = Image.open("c.png")
d = Image.open("d.png")
e = Image.open("e.png")
f = Image.open("f.png")
g = Image.open("g.png")
h = Image.open("h.png")
i = Image.open("i.png")
j = Image.open("j.png")
k = Image.open("k.png")
l = Image.open("l.png")
m = Image.open("m.png")
n = Image.open("n.png")
o = Image.open("o.png")
p = Image.open("p.png")
q = Image.open("q.png")
r = Image.open("r.png")
s = Image.open("s.png")
t = Image.open("t.png")
u = Image.open("u.png")
v = Image.open("v.png")
w = Image.open("w.png")
x = Image.open("x.png")
y = Image.open("y.png")
z = Image.open("z.png")
sp = Image.open("zspace.png")
back = Image.open("zback.png")

switch = True
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/pc/Desktop/tess/tesseract.exe'

def setvar(var,color="black"):
    strvar.set(var)
    tk.Label(win, textvariable= strvar,fg=color).grid(row=2,column=1)

def end():
    switch = False
    win.quit()

def condition(cont):
    width = 50
    height = 0
    newwidth = 0
    for letter in cont:
        if letter == "\n":
            letter = ""
        if letter == "a":
            back.paste(a,(width,height))
            newwidth = a.width
        if letter == "b":
            back.paste(b,(width,height))
            newwidth = b.width
        if letter == "c":
            back.paste(c,(width,height))
            newwidth = c.width
        if letter == "d":
            back.paste(d,(width,height))
            newwidth = d.width
        if letter == "e":
            back.paste(e,(width,height))
            newwidth = e.width
        if letter == "f":
            back.paste(f,(width,height))
            newwidth = f.width
        if letter == "g":
            back.paste(g,(width,height))
            newwidth = g.width
        if letter == "h":
            back.paste(h,(width,height))
            newwidth = h.width
        if letter == "i":
            back.paste(i,(width,height))
            newwidth = i.width
        if letter == "j":
            back.paste(j,(width,height))
            newwidth = j.width
        if letter == "k":
            back.paste(k,(width,height))
            newwidth = k.width
        if letter == "l":
            back.paste(l,(width,height))
            newwidth = l.width
        if letter == "m":
            back.paste(m,(width,height))
            newwidth = m.width
        if letter == "n":
            back.paste(n,(width,height))
            newwidth = n.width
        if letter == "o":
            back.paste(o,(width,height))
            newwidth = o.width
        if letter == "p":
            back.paste(p,(width,height))
            newwidth = p.width
        if letter == "q":
            back.paste(q,(width,height))
            newwidth = q.width
        if letter == "r":
            back.paste(r,(width,height))
            newwidth = r.width
        if letter == "s":
            back.paste(s,(width,height))
            newwidth = s.width
        if letter == "t":
            back.paste(t,(width,height))
            newwidth = t.width
        if letter == "u":
            back.paste(u,(width,height))
            newwidth = u.width
        if letter == "v":
            back.paste(v,(width,height))
            newwidth = v.width
        if letter == "w":
            back.paste(w,(width,height))
            newwidth = w.width
        if letter == "x":
            back.paste(x,(width,height))
            newwidth = x.width
        if letter == "y":
            back.paste(y,(width,height))
            newwidth = y.width
        if letter == "z":
            back.paste(z,(width,height))
            newwidth = z.width
        if letter == " ":
            back.paste(sp,(width,height))
            newwidht = sp.width
        width = width + newwidth
        if width+150 >= back.width:
            height = height + 227
            width = 50
        print(width)
        content = ""
    back.show()

def scnlivecamera():
    switch = True
    url="http://192.168.43.4:8080/shot.jpg"  ##Enter your ip address here
    scaling_factor =0.3
    win.update()
    
    while switch:
        imglink=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp,-1)
        frame = cv2.resize(img, None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
        cv2.imshow('IFT', frame)
        cv2.waitKey(1)
        
        if key.is_pressed("r"):
            path = r"ankit.png"
            cv2.imwrite(path,img)
            content = pytesseract.image_to_string(Image.open(r'%s'%path))
            condition(content)
            switch = False
            cv2.waitKey(1) & 0xFF

def extract():
    setvar("Please Wait!")
    win.update()
##    try:
    check = var.get()
    imgpath = str(e1.get())
    filepath = str(e2.get())

    
    if check:
        case = "w"
        
    else:
        case = "a"

    
    content = pytesseract.image_to_string(Image.open(r'%s'%imgpath))

    file = open(filepath,case)
    file.write(content)
    file.write("\n-------------------------------------\n")
    file.close()
    
    print(content)
    content = content.lower()
    
    setvar("DONE!","green")
    condition(content)
    
##    except:
##        setvar("ERROR!","red")

   
win = tk.Tk()
win.geometry("270x95")
win.title("TxtFromImg")

strvar = tk.StringVar()
var = tk.IntVar(win)

tk.Label(win, text="Path to Image : ").grid(row=0)
tk.Label(win, text="Destination folder : ").grid(row=1)

e1 = tk.Entry(win)
e2 = tk.Entry(win)
e2.insert(0,"ankit.txt")
e1.grid(row = 0,column = 1)
e2.grid(row = 1,column = 1)

che = tk.Checkbutton(win,text="Delete last saved texts",variable=var).grid(row=2,column=0)
but1 = tk.Button(win,text="Extract",command = extract)
but2 = tk.Button(win,text="Scan",command = scnlivecamera,padx=8)
but3 = tk.Button(win,text="Cancel",command = end)
but1.place(x=30,y=67)
but2.place(x=115,y=67)
but3.place(x=200,y=67)
win.mainloop()
