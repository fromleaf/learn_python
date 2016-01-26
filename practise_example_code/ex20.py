# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)
#	print_all(f)

def print_a_line(line_count, f):
	print line_count, f.readline(),

current_file = open(input_file)

print("print all of contents in the file.\n")
print_all(current_file)

print("rewind the file likes a video tape.\n")
rewind_file = current_file
#rewind(current_file)
rewind(rewind_file)

print("print 3 lines in the file")
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
