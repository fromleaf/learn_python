"""
Given a class Pet, write a empty class Cat that inherits from it, 
and a class Dog which has an instance method eat_cat()
which prints the statement dog_name has eaten cat_name , as shown in the following example:

===========================
Cat Name: Kitten
Cat food: Fish
Dog Name: Puppy
Dog food: Meat
Puppy has eaten Kitten
===========================
"""

class Pet(object):
	def __init__(self, name, eats):
		self.name = name
		self.eats= eats

#{Write your code here


class Cat(Pet):
	def __init__(self, name, eats):
		super(Cat, self).__init__(name, eats)
	
class Dog(Pet):
	def __init__(self, name, eats):
		super(Dog, self).__init__(name, eats)

	def eat_cat(self, Cat):
		print("%s has eaten %s" % (self.name, Cat.name))


#}

cat = Cat(raw_input("Cat Name: "), raw_input("Cat food: "))

dog = Dog(raw_input("Dog Name: "), raw_input("Dog food: "))
dog.eat_cat(cat)
