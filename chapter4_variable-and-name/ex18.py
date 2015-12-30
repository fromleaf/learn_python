# -*- coding: utf-8 -*-

def print_two(*args):
	arg1, arg2 = args
	print("execution argument1: %r, execution argument2: %r" % (arg1, arg2))

def print_two_again(arg1, arg2):
	print("execution argument1: %r, execution argument2: %r" % (arg1, arg2))

def print_one(arg1):
	print("execution argument1: %r" % arg1)

def print_none():
	print("Nothing argument")

print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("First")
print_none()

