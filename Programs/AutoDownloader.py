import cv2
import numpy as np
import urllib.request
import string
import time

arr = string.ascii_lowercase
lst = []
for char in arr:
    lst.append(char)
app = "zback"+"zspace"
lst.append("zback")
lst.append("zspace")

for char in lst:
    url = "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Images/%s.png"%char
    imglink=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imglink.read()))
    img = cv2.imdecode(imgNp,-1)
    cv2.imwrite(r"%s.png"%char,img)
    print(char+".png saved")
    time.sleep(1)
