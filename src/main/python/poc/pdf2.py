import PyPDF2
import os

file = "/Users/gopn/Downloads/Appendix_C_from_pdf_reference.pdf"

fb = open(file, 'rb')

reader = PyPDF2.PdfFileReader(fb)

content = ""
for i in range(0,reader.getNumPages()):
    page= reader.getPage(i)
    content =  content + " " + page.extractText()
print(content)

