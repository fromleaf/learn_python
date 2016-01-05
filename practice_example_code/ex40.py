# -*- coding: utf-8 -*-

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy Birthday.",
				"I don't want to 고소",
				"That's enough."])

bulls_on_parade = Song(["Take a pocket that is full of sheel",
					"They come around a family."])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
