#import win32com.client as wincl
import PIL
import pytesseract
import cv2
#import pyttsx3

from espeak import espeak


#from gtts import gTTS

#import os



#from .engine import Engine

from PIL import Image


#engine = pyttsx3.init()


im = Image.open('IMAGES/bold.png')
im.show()



text = pytesseract.image_to_string(im)

print(text)


#------------------------------------------------------

espeak.set_parameter(espeak.Parameter.Rate, 70)

espeak.synth(text) 
while espeak.is_playing:
	pass



#--------------------------------------------------------



#tts = gTTS(text='Good morning', lang='en')

#engine.say(text)
#engine.runAndWait()

#speak = wincl.Dispatch("SAPI.SpVoice")
#speak.Speak(text)
