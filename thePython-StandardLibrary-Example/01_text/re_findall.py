import re

text = 'abbaaabbbbaaaaa'

patter = 'ab'

for match in re.findall(patter, text):
	print 'Found "%s"' % match
