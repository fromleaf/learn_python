# -*- coding: utf-8 -*-

import string

leet = string.maketrans('abegiloprstz', '463611092572')
s = 'The quick brown fox jumped over the lazy dog.'

print "sentence: " + s
print "capwords: " + string.capwords(s)
print "translate: " + s.translate(leet)
print "\n" + "=" * 70 + "\n"

values = { 'var': 'foo' }

t = string.Template("""
		Variable			: $var
		Escape				: $$
		Variable in text	: ${var}iable
		""")

print 'TEMPLATE: ', t.substitute(values)

s = """
Variable				: %(var)s
Escape					: %%
Variable in Text		: %(var)siable
"""
print 'INTERPOLATION: ', s % values
print "\n" + "=" * 70 + "\n"

values = { 'var': 'foo' }
t = string.Template("$var is here but $missing is not provided")
try:
	print 'substitute()			:', t.substitute(values)
except KeyError, err:
	print 'ERROR: ', str(err)

print 'safe_substitute(): ', t.safe_substitute(values)
print "\n" + "=" * 70 + "\n"


