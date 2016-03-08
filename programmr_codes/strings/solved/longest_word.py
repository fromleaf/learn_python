"""
Write a program to find out the longest word in the sentence input by the user.

==========================
Input:
This site is for programming in a lot of languages
Output:
programming
==========================
"""

string = raw_input("Enter your String:") 
 
#write down your logic here
class Word(object):
	def __init__(self, word, length):
		self.word = word
		self.length = length

str_list = string.split(" ")

word_list = []
for i in range(0, len(str_list)):
	temp_word = str_list.pop()
	word = Word(temp_word, len(temp_word))
	word_list.append(word)

from operator import attrgetter
sorted_word_list = sorted(word_list, key=attrgetter('length'))
	
longest_word = sorted_word_list.pop().word
#

print longest_word
