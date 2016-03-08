class Person:
	def __init__(self, name, city):
		self.name = name
		self.city = city

	def report(self):
		print(self.name)
		print(self.city)
# {Write your logic here     

class Programmer(Person):
		
	def __init__(self, name, city, programming_language):
		self.name = name
		self.city = city
		self.programming_language = programming_language
	
	def report(self):
		print(self.name)
		print(self.city)
		print(self.programming_language)

# }
p1 = Programmer(raw_input("Name:"), raw_input("city:"), raw_input("programming language:"))
p1.report()
