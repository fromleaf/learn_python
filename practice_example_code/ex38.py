# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Hold on, the list still doesn't fill 10 items, so let's fix it."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Add: ", next_one
	stuff.append(next_one)
	print "%d item exists in the list." % len(stuff)

print "Let's look it! ", stuff

print "Let's do it using this"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
