# from gtts import gTTS
# import os
# myText = 'Welcome to geeksForGeek'
# language ='en'
# myobj = gTTS(text = myText, lang = language, slow = False)
# myobj.save("Welcome.mp3")
# os.system("mpg321 Welcome.mp3")
import gtts
from playsound import playsound

t1 = gtts.gTTS("Welcome to Rishi World")
# t1.save("welcome.mp3")
playsound("welcome.mp3")
