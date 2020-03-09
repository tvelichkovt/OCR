#setup
#https://github.com/tesseract-ocr/tesseract/wiki
#https://github.com/UB-Mannheim/tesseract/wiki
#PATH !!! pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('outA.jpg') #import os ; cwd = os.getcwd(); files = os.listdir(cwd) ; print("Files in %r: %s" % (cwd, files)) 

text = pytesseract.image_to_string(img, lang="bul")

print(text)

