"""
Write a program which prints the current day,date and time of the system.

==================================
Input:
Current Day, Date and Time (y/n):
y
Output:
Fri Mar 22 13:07:42 2013

Input:
Current Day, Date and Time (y/n):
n
Output:
Thank You
==================================

"""
from time import ctime

x=raw_input("Current Day,Date and Time (y/n):")
	 
if str(x) == 'y' or str(x) == 'Y':
	print(ctime())
elif str(x) == 'n' or str(x) == 'N':
	print('Thank You')
