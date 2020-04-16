import pytesseract
import cv2
import numpy as np
import urllib.request
import keyboard as key
from PIL import Image
import string
import time

ip_add = "192.168.xy.yz:8080"    ###Enter your ip address here###
switch = True

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/pc/Desktop/tess/tesseract.exe'
url="http://"+ip_add+"/shot.jpg"
scaling_factor =0.3
width,height = 50,0
arr = string.ascii_lowercase
arr = arr+" "

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
while True:  
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
    except Exception as e:
        print(e)
        print('''ERROR!\nTo use this feature, you need to download IP webcam from playstore and start server, then open "zlivecamerafile.py" and add your ip address there.
IGNORE IF YOU ALREADY DID.''')
        time.sleep(10)
        break
