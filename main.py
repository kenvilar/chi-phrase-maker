import json

from matchword import if_one_close_match, similarity_check

data = json.load(open('phrases.json', 'r'))


def translate(myWord):
	if myWord in data:
		return data[myWord]
	elif if_one_close_match(myWord, data):
		return similarity_check(myWord, data)
	else:
		return 'Your keywords doesn\'t exist.'


word = input('Enter your keyword/s: ')
translate = translate(word.lower())
print(translate)
