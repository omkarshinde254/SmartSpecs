import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)
engine.say('Sir mmuze placement dedoo.....')
#engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
