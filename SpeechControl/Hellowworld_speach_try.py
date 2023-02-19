from espeak import espeak

espeak.set_parameter(espeak.Parameter.Rate, 120)

espeak.synth('Hello World') 
while espeak.is_playing:
	pass

