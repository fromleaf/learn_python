# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copy from %s to %s." % (from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("Input file is %d byte." % len(indata))

print("Does the file exist? %r" % exists(to_file))	
print("Ready. If you want to continue to press a enter, if you want to cancel to presss 'CTRL-C'")
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Good. Complete all of them.")

out_file.close()
in_file.close()
