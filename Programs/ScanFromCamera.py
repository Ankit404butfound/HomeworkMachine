import cv2
import numpy as np
import urllib.request
import pytesseract
import keyboard as key
from PIL import Image

width = 50
height = 0
newwidth = 0
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
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/pc/Desktop/tess/tesseract.exe'
url="http://192.168.43.1:8080/shot.jpg"
scaling_factor =0.3
dist = 0
fact = 0
count = 0

while True:
        imglink=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp,-1)
        frame = cv2.resize(img, None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
        cv2.imshow('IFT', frame)
        cv2.waitKey(1)
        if key.is_pressed("r"):
            count += 1
            path = r"C:/Users/pc/Desktop/New folder (2)/read.png"
            cv2.imwrite(path,img)
            content = pytesseract.image_to_string(Image.open(r'%s'%path))
            for letter in content.lower():
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
            back.show()
