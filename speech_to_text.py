import speech_recognition as sr

r = sr.Recognizer()
r.dynamic_energy_threshold = True

with sr.Microphone() as source:
	print('Say Something')
	audio = r.listen(source)

try:
	print('You Said : \n' +r.recognize_google(audio))

except Exception as e:
	print (e)
