from tensorpy import image_base
import pyttsx3
from PIL import Image

engine = pyttsx3.init()

img = "popbottle.jpg"
result = image_base.classify(img)

print("\nBest match classification :\n%s\n" %result)


rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

engine.say(result) 

engine.runAndWait()
