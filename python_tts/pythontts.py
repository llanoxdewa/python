from gtts import gTTS
import os

with open("text.txt","r") as fh:
	mytext = fh.read().replace("\n"," ")
bahasa = 'en'

output = gTTS(text=mytext,lang=bahasa,slow=False)

output.save("programtts.mp3")

