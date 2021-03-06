import re

def test_patterns(text, patterns=[]):
	"""Given source text and a list of patterns, look for
	   matches for each pattern within the text and print
	   them to stdout.
	"""
	
	# find patterns and print a result in text
	for pattern, desc in patterns:
		print 'Pattern %r (%s)\n' % (pattern, desc)
		print ' %r' % text
		for match in re.finditer(pattern, text):
			s = match.start()
			e = match.end()
			substr = text[s:e]
			n_backslashes = text[:s].count('a')
			print ' n_backslashes: %d' % n_backslashes
			prefix = '.' * (s + n_backslashes)
			print ' %s%r' % (prefix, substr)
		print
	return

if __name__ == '__main__':
	test_patterns('abbaaabbbbaaaaa',
			[('ab', "'a' followed by 'b'"),
			])
