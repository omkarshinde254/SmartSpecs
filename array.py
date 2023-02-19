names = []
print (names)

names.append("one")
names.append("two")
print (names)

count = 0

while True:
	print ("Enter the input user")
	
	a = input()
	
	names.append(a)
	print (names)
	count +=1
	if(count == 5):
		break

s = list(set(names))
print (s)
