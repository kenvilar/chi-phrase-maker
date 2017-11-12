import json
from matchword import get_match_keyword

data = json.load(open('phrases.json', 'r'))


def translate(myWord):
	if myWord in data:
		return data[myWord]
	elif len(get_match_keyword(myWord, data.keys())) > 0:
		best_match = get_match_keyword(myWord, data.keys())[0]
		yesOrNo = input('Did you mean %s instead? Please enter Y if yes, or N if no. \n' % best_match)
		if yesOrNo == 'Y':
			correctWord = get_match_keyword(myWord, data.keys())[0]
			return data[correctWord]
		elif yesOrNo == 'N':
			return 'Your keywords doesn\'t exist.'
		else:
			return 'Just Y or N only'
	else:
		return 'Your keywords doesn\'t exist.'


word = input('Enter your keyword/s: ')
translate = translate(word.lower())
print(translate)
