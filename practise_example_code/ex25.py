# -*- coding: utf-8 -*-

def break_words(stuff):
	"""This function separates the sentence as word."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""This function orders the words"""
	return sorted(words)

def print_first_word(words):
	"""This function pops the first word and prints it."""
	word = words.pop(0)
	return word

def print_last_word(words):
	"""This function pops the end word and prints it."""
	word = words.pop(-1)
	return word

def sort_sentence(sentence):
	"""This function gets a whole sentence and sorts it and return to be sorted it."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print a first word of the sentence and a last word of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""This function sorts the words in the sentence and prints the first word and the last word."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
