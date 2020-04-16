from PIL import Image
import string

back = Image.open("zback.png")
width,height = 50,0
arr = string.ascii_lowercase
arr = arr+" "

def condn(case):
    global width,height
    print(case)
    cases = Image.open("%s.png"%case)
    back.paste(cases,(width,height))
    newwidth = cases.width
    width = width+newwidth

inp = input()

for letter in inp:
    if letter in arr:
        if letter == " ":
            letter = "zzback"
        condn(letter)
        
back.show()
