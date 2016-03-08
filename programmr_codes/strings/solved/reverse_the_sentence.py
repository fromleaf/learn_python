"""
Write a program to reverse the sentences wordwise

--------------------
Input:
You have entered a wrong domain
Output:
domain wrong a entered have you
-------------------
"""

string = raw_input("Input:").split(" ")
string.reverse()
print ' '.join(string)
