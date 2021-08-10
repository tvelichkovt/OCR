'''
'''

# 1. Imports

from PIL import Image 
from pdf2image import convert_from_path
import pytesseract 


# 1. Conversion into jpeg

pages = convert_from_path('1.pdf', 500)
for page in pages:
    page.save('page_.jpg', 'JPEG')

image_counter = 1
    
for page in pages: 
    filename = "page_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG') 
    image_counter = image_counter + 1

# 2. Save txt file + encoding="utf-8" for Bulgarian /remove for English/
    
filelimit = image_counter-1
outfile = "OCR _From_Pdfs.txt"

f = open(outfile, "a", encoding="utf-8")#, encoding="utf-8") for Bulgarian
#f = open(outfile, "a") for English Language

# 3 Iterate from 1 to total number of pages, Tesseract up + lang="bul"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #, encoding="utf-8") for Bulgarian

for i in range(1, filelimit + 1): 
    filename = "page_"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename), lang="bul")))) #, lang="bul") for Bulgarian
   #text = str(((pytesseract.image_to_string(Image.open(filename))))) #for English Language
    text = text.replace('-\n', '')     #replace every '-\n' to '' or remove the line!
    f.write(text) 
  
f.close() 

