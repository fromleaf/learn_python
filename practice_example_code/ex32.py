# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'mandarin', 'peer', 'apricot']
change = [1, '10 cent', 2, '100 cent', 3, '500 cent']

# first for goes around to follow the lists
for number in the_count:
	print "this number is %d." % number

# same first for
for fruit in fruits:
	print "kind of fruit: %s" % fruit

# mixed list can be went around.
for i in change:
	print "return small money %s" %i

# In addtion, you can make a list, first start to a emtpy list
elements = []

# moreover count 0 to 5 to use range function
for i in range(0, 6):
	print "add %d number to list." % i
	# the list knows append function
	elements.append(i)

# you can print it
for i in elements:
	print "element is %d" % i
