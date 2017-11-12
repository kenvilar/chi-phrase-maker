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
