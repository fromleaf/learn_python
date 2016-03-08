#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
Given a Person class, where each person has a name and a city, write a class Programmer which is a subclass of Person.
A programmer should have a name, city, and a programming language. 
Write a report() method for programmer which prints all his data, each on a single line. 
Use the overriding principle.
"""

class Person:
	name = "default_name"
	city = "default_city"
	
	def __init__(self, _name, _city):
		self.name = _name
		self.city = _city

	def info(self):
		print "Person is  %s" % self.name
		print "Person has lived in %s" % self.city
		


class Programmer(Person):
	programming_language = "default_programming_language"

	def __init__(self, _name, _city, _programming_language):
		self.name = _name
		self.city = _city
		self.programming_language = _programming_language

	def report(self):
		print "Programmer's Language is %s" % self.programming_language


programmer = Programmer("Tom", "Seoul", "C")
programmer.info()
programmer.report()
