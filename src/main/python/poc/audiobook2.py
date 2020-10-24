from gtts import gTTS
import re

file = "/Users/gopn/gerrit/ngab/src/main/python/poc/output.txt"
fb = open(file, 'rb')
content = ""

if '.txt' in file:
    by = fb.readlines()
    for i in by:
        text = i.decode("utf-8")
        print("-",text.strip(),"-")
    content = " ".join(i.decode("utf-8").strip() for i in by)

content = content.replace("-\n", "")
content = content.replace("\n", " ")
content = re.sub('\s+', ' ', content)
print(content)


with open('test.mp3', 'wb') as f:
    for token in content.split("."):
        print(token+".")
        engine1 = gTTS(token.strip(), lang='ta')
        engine1.write_to_fp(f)
