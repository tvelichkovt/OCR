# 1. Imports

from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path

# 2. Conversion into jpeg

pages = convert_from_path('bgregistryagency3pages.pdf', 500)
for page in pages:
    page.save('page_.jpg', 'JPEG')

image_counter = 1
    
for page in pages: 
    filename = "page_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG') 
    image_counter = image_counter + 1

# 3. Save txt file
    
filelimit = image_counter-1
outfile = "OCR _From_Pdf.txt"

f = open(outfile, "a", encoding="utf-8")

# 4 Iterate from 1 to total number of pages 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #, encoding="utf-8") for Bulgarian

for i in range(1, filelimit + 1): 
    filename = "page_"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename), lang="bul")))) #, , lang="bul") for Bulgarian
    text = text.replace('-\n', '')     #replace every '-\n' to ''
    f.write(text) 
  
f.close() 

