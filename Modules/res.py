
import os, os.path

DIR = 'rani'
x = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
count = 0
c=0
m=0
a1=0
a2=0
a3=0
l=0
r=0
d=0
for i in range(0,x):
    import cv2
    import pytesseract
    import PIL
    from PIL import Image

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = 'rani/ravi'+i
    imge = Image.open(img)
    data = pytesseract.image_to_string(imge)
    if(data=="FORWARD,"):
        count += 1
        if (count != 0):
            l = 1
            r = 0
    elif(data=="FORWARD."):
        c += 1
        if (c != 0):
            r = 1
            l = 0
    elif(data=="FORWARD,."):
        m += 1
        if (m != 0):
            d = 1
            r = 0
            l = 0
    elif(data=="FORWARD"):
        if (l == 1):
            l = 0
            a1 += 1
            l = 0

        if (r == 1):
            r = 0
            a2 += 1
            r = 0
        if (d == 1):
            d = 0
            a3 += 1
            d = 0

print(a1,a2,a3)



