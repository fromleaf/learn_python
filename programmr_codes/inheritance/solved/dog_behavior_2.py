class Animal(object):
	def __init__(self, behavior):
		self.behavior = behavior
		print("Animal constructor")

	def getbehavior(self):
		for i in self.behavior:
			print (i)


class Dog(Animal):
	def __init__(self, behavior):
		super(Dog,self).__init__(behavior)
		print ("Dog constructor")
#{Write your code here    
	

dog_acting1 = ["Animal run", "Dog barks"]
dog1 = Dog(dog_acting1)
dog1.getbehavior()

dog_acting2 = ["Animal talks", "Dog chase cat"]
dog2 = Dog(dog_acting2)
dog2.getbehavior()





#}
