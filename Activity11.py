temp = eval(input("Enter temperature --> "))

if temp >= 1 and temp <= 20:
	print("Temperature outside is cold")
elif temp >= 21 and temp <= 30:
	print("Temperature outside is lukewarm")
elif temp >= 31 and temp <= 40:
	print("Temperature outside is warm")
elif temp >= 41 and temp <= 50:
	print("Temperature outside is hot")
if temp >= 50: 
	print("Temperature outside is boiling hot")

else:
	print("invalid Temperature")
