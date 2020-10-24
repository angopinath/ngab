from pdfminer.high_level import *

pages = extract_pages('/Users/gopn/Downloads/ManamThudikkum_a4.pdf')
print(type(pages), pages)