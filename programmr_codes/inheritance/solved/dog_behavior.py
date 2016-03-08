"""
Write a program that creates two dogs but they have different behavior.
The program must display its corresponding actions like below:

-------------------
Animal constructor
Dog constructor
Animal run
Dog barks
Animal constructor
Dog constructor
Animal talks
Dog chase cat
-------------------
"""

class Animal(object):
	def __init__(self):
		print("Animal constructor")

	def run(self):
		print("Animal run")

	def talks(self):
		print("Animal talks")

	

class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Dog constructor")

	def barks(self):
		print("Dog barks")

	def chase_cat(self):
		print("Dog chase cat")

d1 = Dog()
d1.run()
d1.barks()

d2 = Dog()
d2.talks()
d2.chase_cat()
