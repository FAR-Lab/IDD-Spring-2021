import webcolors

screenColor= None

while not screenColor:
	try:
		screenColor = list(webcolors.name_to_rgb(input('Type the name of a color and hit enter: ')))
	except ValueError:
		print("whoops I don't know that one")
print(*screenColor)