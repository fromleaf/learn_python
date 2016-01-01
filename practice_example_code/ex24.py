# -*- coding: utf-8 -*-

print "Let's practice all of things."
print "Using \\ you 'must know' new line \n or \t tab that is escape array."

poem = """
\t The lovley world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------------"
print poem
print "--------------------"

five = 10 - 2 + 3 - 6
print "This result is five.: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "Start point: %d" % start_point
print "There are %d beans, %d jars, %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "You should do to like this."
print "There are %d beans, %d jars, %d crates." % secret_formula(start_point)
