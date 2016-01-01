# -*- coding: utf-8 -*-

def cheese_and_cracker(cheese_count, boxes_of_crackers):
	print("There are %d pieces of cheese!" % cheese_count)
	print("There are %d boxes!" % boxes_of_crackers)
	print("These are enough having a party!!")
	print("Bring a blanket.\n")

print("You can send argument to function directly.")
cheese_and_cracker(20, 30)

print("You can also use script's argument")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_cracker(amount_of_cheese, amount_of_crackers)

print("You can count in the function.")
cheese_and_cracker(10 + 20, 5 + 6)

print("You can use argument and count it, after merge the numbers and arguments.")
cheese_and_cracker(amount_of_cheese + 1000, amount_of_crackers + 10000)
