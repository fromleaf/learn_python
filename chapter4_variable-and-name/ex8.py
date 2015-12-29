# -*- coding: utf-8 -*-

formatter = "%s %s %s %s"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
		"I have this.",
		"You just are writing that.",
		"However I don't 'sing'.",
		"Anyway, Good night."
))

formatter2 = "%r %r %r %r"
print(formatter2 % (
		"I have this.",
		"You just are writing that.",
		"However I don't 'sing'.",
		"Anyway, Good night."
))
