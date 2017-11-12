import json

data = json.load(open('phrases.json', 'r'))


def translate(myWord):
	if myWord in data:
		return data[myWord]
	else:
		return 'Your keywords doesn\'t exist.'


myWord = input('Enter your keyword/s: ')
translate = translate(myWord)
print(translate)
