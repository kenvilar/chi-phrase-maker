import json

data = json.load(open('phrases.json', 'r'))


def translate(word):
	if word in data:
		print(data[word])
	else:
		print('Your keywords doesn\'t exist.')


translate('Hello')
