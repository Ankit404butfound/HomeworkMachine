from PIL import Image
import cv2
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
text = input().lower()
text = str(text)
for letter in text:
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
back.show()
