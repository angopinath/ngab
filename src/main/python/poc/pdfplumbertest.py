import pdfplumber

pdf = pdfplumber.open('/Users/gopn/Downloads/Devagiyin_Kanavan.pdf')
content= ''
for page in pdf.pages:
    for c in page.chars:
        content=content + c['text']
print(content)
