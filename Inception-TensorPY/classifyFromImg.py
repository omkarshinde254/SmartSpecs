from tensorpy import image_base
from espeak import espeak


print('Enter the URL or Path of Image :-')
img = input()

result = image_base.classify(img)

print("\nBest match classification :\n%s\n" %result)


espeak.set_parameter(espeak.Parameter.Rate, 130)

espeak.synth(result) 
while espeak.is_playing:
	pass

