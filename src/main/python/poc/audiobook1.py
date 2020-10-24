import pyttsx3 as tts
import re

engine = tts.init()

import PyPDF2
import os

file = "/Users/gopn/gerrit/ngab/src/main/python/poc/output.txt"
fb = open(file, 'rb')
content = ""

if '.pdf' in file:
    reader = PyPDF2.PdfFileReader(fb)
    for i in range(1, reader.getNumPages()):
        page= reader.getPage(i)
        content = content + " " + page.extractText()

if '.txt' in file:
    bytes = fb.read()
    content = bytes.decode('utf-8')

content = content.replace("-\n", "")
content = content.replace("\n", " ")
content = re.sub('\s+', ' ', content)
print(content)
print(engine.getProperty('rate'))
engine.setProperty("rate", 120)
engine.say(content)
#engine.save_to_file(content, 'the-last-leaf.mp3')
engine.runAndWait()