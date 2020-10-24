from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import sys
import os


file = '/mnt/c/Users/gopn/Downloads/Devagiyin_Kanavan.pdf'
images = []
base_path='/mnt/c/Users/gopn/gerrit/ngab/src/main/python/poc/'

pages = convert_from_path(file)
for index, page in enumerate(pages):
    image = base_path + "page_"+str(index)+".jpg"
    page.save(image, 'JPEG')
    images.append(image)


output = base_path + 'output.txt'
output_file = open(output, 'a')
print(len(images))
for i in images:
    print('page no:',i)
    text = str(pytesseract.image_to_string(Image.open(i), lang='tam'))
    print(text)
    output_file.write(text)
output_file.close()



