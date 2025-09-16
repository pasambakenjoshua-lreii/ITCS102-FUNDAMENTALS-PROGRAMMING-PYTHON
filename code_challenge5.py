print("Welcome to the manga recommender!")
print("pls insert your preference to find your manga")

Genre = input(" What is prefered genre? (shonen, slice of life, mecha):")
Duration = input(" what duration should the manga be? (short, medium, long):")
Time = input("Which year? (2000s, 2010s):")

if Genre == 'shonen' and Duration == 'short' and Time == '2000':
	print("The manga recommend for this is 'Yu Yu Hakusho' ")
elif Genre == 'shonen' and Duration == 'short' and Time == '2010':
	print("The manga recommend for this is 'Bamboo Blade' ")
elif Genre == 'shonen' and Duration == 'medium' and Time == '2000':
	print("The manga recommend for this is 'Rurouni Kenshin' ")
elif Genre == 'shonen' and Duration == 'medium' and Time == '2010':
	print("The manga recommend for this is 'Blue Exorcist' ")
elif Genre == 'shonen' and Duration == 'long' and Time == '2000':
	print("The manga recommend for this is 'One Piece' ")
elif Genre == 'shonen' and Duration == 'long' and Time == '2010':
	print("The manga recommend for this is 'Fairy Tail' ")

if Genre == 'slice of life' and Duration == 'short' and Time == '2000':
	print("The manga recommended for this is 'Yotsuba&!' ")
elif Genre == 'slice of life' and Duration == 'short' and Time == '2010':
	print("The manga recommended for this is 'Barakamon' ")
elif Genre == 'slice of life' and Duration == 'medium' and Time == '2000':
	print("The manga recommended for this is 'Honey and Clover' ")
elif Genre == 'slice of life' and Duration == 'medium' and Time == '2010':
	print("The manga recommended for this is 'March Comes in Like a Lion' ")
elif Genre == 'slice of life' and Duration == 'long' and Time == '2000':
	print("The manga recommended for this is 'Aria' ")
elif Genre == 'slice of life' and Duration == 'long' and Time == '2010':
	print("The manga recommended for this is 'Silver Spoon' ")

if Genre == 'mecha' and Duration == 'short' and Time == '2000':
	print("The manga recommended for this is 'RahXephon' ")
elif Genre == 'mecha' and Duration == 'short' and Time == '2010':
	print("The manga recommended for this is 'ID-0' ")
elif Genre == 'mecha' and Duration == 'medium' and Time == '2000':
	print("The manga recommended for this is 'Zegapain' ")
elif Genre == 'mecha' and Duration == 'medium' and Time == '2010':
	print("The manga recommended for this is 'Knights of Sidonia' ")
elif Genre == 'mecha' and Duration == 'long' and Time == '2000':
	print("The manga recommended for this is 'Getter Robo Saga' ")
elif Genre == 'mecha' and Duration == 'long' and Time == '2010':
	print("The manga recommended for this is 'Valvrave the Liberator' ")

else:
	print("Invalid input. I can only provide this at the moment (shonen, slice of life, mecha)")
