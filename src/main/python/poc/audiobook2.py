from .tts.mytts import gTTS
import re

file = "/Users/gopn/gerrit/ngab/src/main/python/poc/output_short.txt"
audio_file = "/Users/gopn/gerrit/ngab/audiobooks/test1.mp3"
fb = open(file, 'rb')
content = ""

if '.txt' in file:
    by = fb.readlines()
    for i in by:
        text = i.decode("utf-8")
        print(i,"-",text.strip(),"-")
    content = " ".join(i.decode("utf-8").strip() for i in by)

content = content.replace("-\n", "")
content = re.sub(r'[\n]{2,}', '. ', content)
content = re.sub(r'[\s]{2,}', ' ', content)
content = " ".join(content.splitlines())
content = re.sub(r'[\\.]{2,}', '.', content)
content = content.replace('.,', ',')
print(len(content), content)


with open(audio_file, 'wb') as f:
    for token in content.split("."):
        print(token+".")
        engine1 = gTTS(token.strip(), lang='ta', speed=0.5)
        engine1.write_to_fp(f)
