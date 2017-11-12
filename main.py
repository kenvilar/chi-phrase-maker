import json

data = json.load(open('phrases.json', 'r'))


def translate(word):
	if word in data:
		return data[word]
	else:
		return 'Your keywords doesn\'t exist.'


word = input('Enter your keyword/s: ')
translate = translate(word)
print(translate)
