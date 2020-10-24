import pyttsx3 as tts
import re

file = "/mnt/c/Users/gopn/gerrit/ngab/src/main/python/poc/output_short.txt"
fb = open(file, 'rb')
content = ""

if '.txt' in file:
    by = fb.readlines()
    content = " ".join(i.decode("utf-8").strip() for i in by)

content = content.replace("-\n", "")
content = content.replace("\n", " ")
content = re.sub('\s+', ' ', content)
print(content)

engine = tts.init()
print(engine.getProperty("rate"))
print(engine.getProperty("volume"))
print(engine.getProperty("voices"))
for voice in engine.getProperty("voices"):
    print(voice.id)

engine.save_to_file("test", '/mnt/c/Users/gopn/gerrit/ngab/src/main/python/poc/test1.wav')
engine.runAndWait()
print("success")
