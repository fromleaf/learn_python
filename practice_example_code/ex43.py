# -*- coding: utf-8 -*-

## Animal is one of object (is-a) 
class Animal(object):
	pass

## Dog is one of Animal.
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has a name.
		self.name = name

## Cat is one of Animal
class Cat(Animal):
	
	def __init__(self, name):
		## Cat has a name.
		self.name = name

## Person is one of object
class Person(object):
	
	def __init__(self, name):
		## Person has a name
		self.name = name

		## Person has what kind of dog (has-a)
		self.pet = None

## Employee in one of Person
class Employee(Person):
	
	def __init__(self, name, salary):
		## What is kind of spell??
		super(Employee, self).__init__(name)
		## Employee has a salary.
		self.salary = salary

## Fish is one of object
class Fish(object):
	pass

## Salmon is one of Fish
class Salmon(Fish):
	pass

## Halibut is one of Fish
class Halibut(Fish):
	pass

## rover is one of Dog. (is-a)
rover = Dog("Rover")

## satan is one of Cat. (is-a)
satan = Cat("Satan")

## Mary is one of Person. (is-a)
mary = Person("Mary")

## Satan is Mary's pet.
mary.pet = satan

## Frank is one of employee, and his salary is 120000.
frank = Employee("Frank", 120000)

## Rover is Frank's pet.
frank.pet = rover

## Flipper is one of Fish.
flipper = Fish()

## Crouse is one of Salmon
crouse = Salmon()

## Harry is one of Halibut
harry = Halibut()
