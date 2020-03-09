#https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

#https://github.com/UB-Mannheim/tesseract/wiki (install tesseract-ocr-w64-setup-v5.0.0-alpha.20200223.exe) ; +add path C:\Program Files\Tesseract-OCR
#pip install pytesseract
#https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
#pip install PIL #pip install Pillow ; #from PIL import Image
#pip install pytesseract
#pip install pdf2image
#pip apt-get install tesseract-ocr
#pip install image
#pip install --no-index -f http://effbot.org/downloads/ -U PIL --trusted-host effbot.org
#conda install -c conda-forge poppler
#pip install tesseract


from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path



pages = convert_from_path('receipt1.pdf', 500)


for page in pages:
    page.save('out.jpg', 'JPEG')
    
image_counter = 1
   
    
for page in pages: 
  
    # Declaring filename for each page of PDF as JPG 
    # For each page, filename will be: 
    # PDF page 1 -> page_1.jpg 
    # PDF page 2 -> page_2.jpg 
    # PDF page 3 -> page_3.jpg 
    # .... 
    # PDF page n -> page_n.jpg 
    filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system 
    page.save(filename, 'JPEG') 
  
    # Increment the counter to update filename 
    image_counter = image_counter + 1
    
filelimit = image_counter-1
outfile = "out_text.txt"

f = open(outfile, "a") 

# Iterate from 1 to total number of pages 
for i in range(1, filelimit + 1): 
  
    # Set filename to recognize text from 
    # Again, these files will be: 
    # page_1.jpg 
    # page_2.jpg 
    # .... 
    # page_n.jpg 
    filename = "page_"+str(i)+".jpg"
          
    # Recognize the text as string in image using pytesserct 
    text = str(((pytesseract.image_to_string(Image.open(filename))))) 
  
    # The recognized text is stored in variable text 
    # Any string processing may be applied on text 
    # Here, basic formatting has been done: 
    # In many PDFs, at line ending, if a word can't 
    # be written fully, a 'hyphen' is added. 
    # The rest of the word is written in the next line 
    # Eg: This is a sample text this word here GeeksF- 
    # orGeeks is half on first line, remaining on next. 
    # To remove this, we replace every '-\n' to ''. 
    text = text.replace('-\n', '')     
  
    # Finally, write the processed text to the file. 
    f.write(text) 
  
# Close the file after writing all the text. 
f.close() 

