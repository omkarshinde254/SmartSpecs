from tensorpy import image_base
import pyttsx3

engine = pyttsx3.init()


print('Enter the URL or Path of Image :-')
img = input()

result = image_base.classify(img)

print("\nBest match classification :\n%s\n" %result)


rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

engine.say(result) 

engine.runAndWait()
