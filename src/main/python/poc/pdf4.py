import PyPDF4

file = "/Users/gopn/Downloads/python-tricks-buffet-awesome-features.pdf"

fb = open(file, 'rb')

reader = PyPDF4.PdfFileReader(fb)

content = ""
for i in range(0, reader.getNumPages()):
    page= reader.getPage(i)
    content =  content + " " + page.extractText()
print(content)