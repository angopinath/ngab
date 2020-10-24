from pdfrw import PdfFileReader

file = PdfFileReader("/Users/gopn/Downloads/python-tricks-buffet-awesome-features.pdf")

print(file.keys())
print(file.items())
for page in file.pages:
    content = page.Contents
    print(type(content))
    print(content)
