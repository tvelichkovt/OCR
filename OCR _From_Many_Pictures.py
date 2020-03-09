# 1. Imports

from PIL import Image 
import pytesseract,fnmatch,os

# 2. Image Counter

image_counter = len(fnmatch.filter(os.listdir(os.getcwd()),'*.jpg'))


# 3. Save txt file + encoding="utf-8" for Bulgarian /remove for English/
    
filelimit = image_counter-1
outfile = "OCR _From_Many_Pictures.txt"

f = open(outfile, "a", encoding="utf-8")#, encoding="utf-8") for Bulgarian
#f = open(outfile, "a") for English Language

# 4 Iterate from 1 to total number of pages, Tesseract up + lang="bul"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #, encoding="utf-8") for Bulgarian

for i in range(1, filelimit + 1): 
    filename = "page_"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename), lang="bul")))) #, lang="bul") for Bulgarian
   #text = str(((pytesseract.image_to_string(Image.open(filename))))) #for English Language
    text = text.replace('-\n', '')     #replace every '-\n' to '' or remove the line!
    f.write(text) 
  
f.close() 

