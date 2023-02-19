import speech_recognition as sr
from os import system
import pyttsx3

r = sr.Recognizer()
r.dynamic_energy_threshold = True

with sr.Microphone() as source:
	print('Say Something')
	audio = r.listen(source)

try:
	print('You Said : \n' +r.recognize_google(audio))

except Exception as e:
	print (e)

if "video" in r.recognize_google(audio):
	system('python3 videotry.py')
if "hello" in r.recognize_google(audio):
	system('python3 Hellowworld_speach_try.py')
if "text" in r.recognize_google(audio):
	system('python3 pyttsxa.py')

