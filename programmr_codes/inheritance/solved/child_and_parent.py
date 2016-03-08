"""
Write a program that uses inheritance to display the output as shown below. 
The program should run the constructors of the classes and use their respective print statements.

=========================
Parent constructor
Child constructor
I am the child class
I am the parent class
=========================

"""
class Parent(object):
	def __init__(self):
		print("Parent constructor")
					        
	def classDetail(self):
		print ("I am the parent class")
									        
#{Write your code here           
class Child(Parent):
	def __init__(self):
		super(Child, self).__init__()
		print("Child constructor")
	
	def classDetail(self):
		print("I am the child class")
		super(Child, self).classDetail()

#}        
									    
result = Child()
result.classDetail()
