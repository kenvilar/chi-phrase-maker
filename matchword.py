from difflib import SequenceMatcher
from heapq import nlargest as _nl


def get_match_keyword(word, possibilities, n = 3, cutoff = 0.6):
	if not n > 0:
		raise ValueError("n must be > 0: %r" % (n,))
	if not 0.0 <= cutoff <= 1.0:
		raise ValueError("cutoff must be in [0.0, 1.0]: %r" % (cutoff,))
	result = []
	s = SequenceMatcher()
	s.set_seq2(word)
	for x in possibilities:
		s.set_seq1(x)
		if s.real_quick_ratio() >= cutoff and \
						s.quick_ratio() >= cutoff and \
						s.ratio() >= cutoff:
			result.append((s.ratio(), x))

	result = _nl(n, result)
	return [x for score, x in result]


def if_one_close_match(word, data):
	if len(get_match_keyword(word, data.keys())) > 0:
		return True
	else:
		return False


def similarity_check(myWord, data):
	best_match = get_match_keyword(myWord, data.keys())[0]
	yesOrNo = input('Did you mean %s instead? Please enter Y if yes, or N if no. \n' % best_match)
	if yesOrNo.lower() == 'y':
		correctWord = get_match_keyword(myWord, data.keys())[0]
		return data[correctWord]
	elif yesOrNo.lower() == 'n':
		return 'Your keywords doesn\'t exist.'
	else:
		return 'Just Y or N only'
