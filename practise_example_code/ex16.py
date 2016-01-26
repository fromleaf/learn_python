# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print("To try to delete %r file." % filename)
print("If you want to cancel, press 'CTRL-C(^C)'.")
print("If you want to countinue, press 'Return'.")

raw_input("?")

print("To be opening file...")
target = open(filename, 'w')

print("Delete contents of file. Bye!")
target.truncate()

print("Now, I'm going to ask to write contents of file.")

line1 = raw_input("the 1 line: ")
line2 = raw_input("the 2 line: ")
line3 = raw_input("the 3 line: ")

print("These lines is written on the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finally, close the file")
target.close()
