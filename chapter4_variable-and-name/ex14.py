# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi~! %s, I'm %s script." %(user_name, script))
print("I'll ask some question to you.")
print("%s, do you like me??" % user_name)
likes = raw_input(prompt)

print("%s, where do you live??" % user_name)
lives = raw_input(prompt)

print("What kind of computer do you have??")
computer = raw_input(prompt)


print ("""
	It's OK. You answered question that do you like me '%s'.
	You live '%s'. I don't know where it is.
	Furthermore You have a '%s' computer. It's cool.
	""" % (likes, lives, computer))

