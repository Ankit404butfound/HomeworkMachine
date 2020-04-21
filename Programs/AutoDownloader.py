import cv2
import numpy as np
import urllib.request
import string
import time

arr = string.ascii_lowercase
arr = string.ascii_letters
arr = arr + string.digits + "+,.-? "

def down(char):
    url = "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/%s"%char
    imglink=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imglink.read()))
    img = cv2.imdecode(imgNp,-1)
    cv2.imwrite(r"%s"%char,img)
    print(char+" saved")
print(arr)
for letter in arr:
    if letter == " ":
        letter = "zspace"
    if letter.isupper():
        letter = "c"+letter.lower()
    if letter == ",":
        letter = "coma"
    if letter == ".":
        letter = "fs"
    if letter == "?":
        letter = "que"
    try:
        down(letter+".png")
    except:
        down(letter+".PNG")
        print("Handled")
    time.sleep(1)
down("zback.png")

