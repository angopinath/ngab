from gtts import gTTS
import os
from io import BytesIO

mp3 = BytesIO()
engine1 = gTTS("சோதனை", lang='ta')
engine2 = gTTS("காலை வணக்கம்", lang='ta')

engine1.write_to_fp(mp3)
engine2.write_to_fp(mp3)

#with open('test.mp3', 'wb') as f:
#    engine1.write_to_fp(f)
#    engine2.write_to_fp(f)
