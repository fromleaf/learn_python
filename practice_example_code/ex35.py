# -*- coding: utf-8 -*-

from sys import exit

def gold_room():
	print "The room is full of gold. How much do you get it?"

	next = raw_input(">")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Human, you need to learn about counting number")

	if how_much < 50:
		print "Good, you are not wanting too much. You won!"
	else:
		dead("Greeding person. You like a idiot.")

def bear_room():
	print "There is a bear."
	print "The bear takes honey full in the pot."
	print "The fat bear is in front of the other door."
	print "How does the bear make to move?"
	bear_moved = False

	while True:
		next = raw_input(">")

		if next == "still honey":
			dead("The bear look at you, and hit your cheek that likes to fly from your face.")
		elif next == "make fun of the bear" and not bear_moved:
			print "The bear move to side door. You can go out."
			bear_moved = True
		elif next == "open the door" and bear_moved:
			gold_room()
		else:
			print "What did you say?"

def cthulhu_room():
	print "You can see the Cthulhu who is king of devils."
	print "The lord, that, anyway it looks you, and you'are going to being crazy."
	print "Do you decide whether you run away from it for your life or it will have your head."

	next = raw_input(">")

	if "run away" in next:
		start()
	elif "eat" in next:
		daed("Hm, it's delicious!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in the dark room."
	print "There are two door that are left side or right side in the room."
	print "which do you want to choose the door?"

	next = raw_input(">")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("I walked around the doors, and I'm dead because I was getting hungry.")

start()
		
