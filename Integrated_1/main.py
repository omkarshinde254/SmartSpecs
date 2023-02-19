import speech_recognition as sr
from os import system
import pyttsx3

r = sr.Recognizer()
r.dynamic_energy_threshold = True

while True:
	with sr.Microphone() as source:
		print('Say Something')
		audio = r.listen(source)
		#r.adjust_for_ambient_noise(source, duration = 1)
	
	try:
		print('You Said : \n' +r.recognize_google(audio))
	
	except Exception as e:
		print (e)
	
	if "face" in r.recognize_google(audio):
		system('python3 face_Detector.py')
	elif "text" in r.recognize_google(audio):
		system('python3 livefeedSpeeechN.py')
	elif "object" in r.recognize_google(audio):
		system('python3 contry.py')
	elif "capture" in r.recognize_google(audio):
		system('python3 PicCap.py')
	elif "tensor" in r.recognize_google(audio):
		system('python3 classifyImage.py')



	if "quit" in r.recognize_google(audio):
		break
