# 1. Imports

from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path


    
filelimit = 3
outfile = "OCR _From_Pdf.txt"

f = open(outfile, "a", encoding="utf-8")#, encoding="utf-8") for Bulgarian

# 4 Iterate from 1 to total number of pages, Tesseract up + lang="bul"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #, encoding="utf-8") for Bulgarian

for i in range(1, filelimit + 1): 
    filename = "page_"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename), lang="bul")))) #, lang="bul") for Bulgarian
    text = text.replace('-\n', '')     #replace every '-\n' to '' or remove the line!
    f.write(text) 
  
f.close() 

