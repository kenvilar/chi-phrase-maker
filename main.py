import json
from matchword import get_match_keyword

data = json.load(open('phrases.json', 'r'))


def translate(myWord):
	if myWord in data:
		return data[myWord]
	elif len(get_match_keyword(myWord, data.keys())) > 0:
		return 'Did you mean %s instead?' % get_match_keyword(myWord, data.keys())[0]
	else:
		return 'Your keywords doesn\'t exist.'


word = input('Enter your keyword/s: ')
translate = translate(word.lower())
print(translate)
