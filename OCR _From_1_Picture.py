'''
'''

# 1. Imports

from PIL import Image
import pytesseract

# 2. Tesseract up + lang="bul" for Bulgarian /remove for English/

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

jpgfile = Image.open('bgregistryagency1page.jpg') #import os ; cwd = os.getcwd(); files = os.listdir(cwd) ; print("Files in %r: %s" % (cwd, files)) 

#text = pytesseract.image_to_string(jpgfile)
text = pytesseract.image_to_string(jpgfile, lang="bul") #, (img, lang="bul")

#print(text)

# 3. Save txt file utf-8/Bulgarian

with open('OCR _From_1_Picture.txt', 'w', encoding="utf-8") as f: #, encoding="utf-8") for Bulgarian
    print(text, file=f)

