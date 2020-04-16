import pytesseract
import tkinter as tk
import numpy as np
import urllib.request
import keyboard as key
from PIL import Image
import string
import os
import time

width = 50
height = 0
newwidth = 0
switch = True
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/pc/Desktop/tess/tesseract.exe'
try:
    back = Image.open("zback.png")
except:
    print("Image not found, download AutoImgDownloader.py file and run it.")
    time.sleep(5)
    exit()
    
width,height = 50,0
arr = string.ascii_lowercase
arr = arr+" "
print(arr)

def setvar(var,color="black"):
    strvar.set(var)
    tk.Label(win, textvariable= strvar,fg=color).grid(row=2,column=1)
    

def casecheck(case):
    global width,height
    print(width,height)
    #print(case)
    cases = Image.open("%s.png"%case)
    back.paste(cases,(width,height))
    newwidth = cases.width
    width = width + newwidth
    #print(width,back.width)

def end():
    file = open("zanotherankit.txt","w")
    file.write("exit")
    file.close()
    win.quit()

def condition(cont):
    global arr,width,height,newwidth
    
    string = cont.split()
    const = " "
    cont = const.join(string)
    for letter in cont:
        if letter in arr:
            if letter == " ":
                letter = "zspace"
            if width + 150 >= back.width:
                height = height + 227
                width = 50
                print(width,height,newwidth)   
            casecheck(letter)
    width,height = 50,0 
    back.show()

def scnlivecamera():
    setvar("Please Wait!")
    condn = True
    os.startfile("zlivecamerafile.py")
    while condn:
        file = open("zanotherankit.txt")
        cont = file.read()
        if cont == "working":
            setvar("DONE!","green")
            condn = False
        
    

def extract():
    setvar("Please Wait!")
    win.update()
    try:
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
    
    except:
        setvar("ERROR!","red")
   
win = tk.Tk()
win.geometry("290x95")
win.title("TxtFromImg")

strvar = tk.StringVar()
var = tk.IntVar(win)

tk.Label(win, text="Path to Image : ").grid(row=0)
tk.Label(win, text="Destination folder : ").grid(row=1)

e1 = tk.Entry(win)
e2 = tk.Entry(win)
e2.insert(0,"zankit.txt")
e1.grid(row = 0,column = 1)
e2.grid(row = 1,column = 1)

che = tk.Checkbutton(win,text="Delete last saved texts",variable=var).grid(row=2,column=0)
but1 = tk.Button(win,text="Extract",command = extract)
but2 = tk.Button(win,text="Scan",command = scnlivecamera,padx=8)
but3 = tk.Button(win,text="Cancel",command = end)
but1.place(x=30,y=67)
but2.place(x=115,y=67)
but3.place(x=200,y=67)
try :
    file = open("zlivecamerafile.py")
    file2 = open("zanotherankit.txt")
    cont = file2.read()
    print(cont)
    if cont == "error":
        setvar("Prgm was forcefully closed!","orange")
    file2.close()
except:
    file = open("zlivecamerafile.py","w")
    file.write("""import pytesseract
import cv2
import numpy as np
import urllib.request
import keyboard as key
from PIL import Image
import string
import time
ip_add = "192.168.xy.yz:8080"    ###Enter your ip address here###
switch = True
file = open("zanotherankit.txt","w")
file.write("working")
file.close()
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/pc/Desktop/tess/tesseract.exe'
url="http://"+ip_add+"/shot.jpg"
scaling_factor =0.3
width,height = 50,0
arr = string.ascii_lowercase
arr = arr+" "
print(arr)

def casecheck(case):
    global width,height
    print(case)
    cases = Image.open("%s.png"%case)
    back.paste(cases,(width,height))
    newwidth = cases.width
    width = width + newwidth
    if width + 150 >= back.width:
        height = height + 227
        width = 50

def condition(cont):
    global arr
    string = cont.split()
    const = " "
    cont = const.join(string)
    width = 50
    height = 0
    newwidth = 0
    for letter in cont:
        if letter in arr:
            if letter == " ":
                letter = "zspace"
                
            casecheck(letter)
    back.show()
    back.close()
    return width,height,newwidth

while switch:
    file = open("zanotherankit.txt","r")
    switch = file.read()
    if switch == "exit":
        switch = False
        
    try:
        imglink=urllib.request.urlopen(url) 
        imgNp=np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp,-1)
        frame = cv2.resize(img, None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
        cv2.imshow('IFT', frame)
        cv2.waitKey(1)
        if key.is_pressed("r"):
            back = Image.open("zback.png")
            width = 50
            height = 0
            newwidth = 0
            path = r"zankit.png"
            cv2.imwrite(path,img)
            content = pytesseract.image_to_string(Image.open(r'%s'%path))
            condition(content)
            cv2.waitKey(1) & 0xFF

    except:
        file = open("zanotherankit.txt","w")
        file.write("error")
        file.close()
        switch = False
        print('''ERROR!\nTo use this feature, you need to download IP webcam from playstore and start server, then open "zlivecamerafile.py" and add your ip address there.
IGNORE IF YOU ALREADY DID.''')
        time.sleep(10)""")
    
    file.close()
    file = open("zanotherankit.txt","w")
    file.write("exit")
    file.close()
win.mainloop()
