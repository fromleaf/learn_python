"""
Write a program which determines whether a given string is palindrome or not.

========================
Input:
Please insert a word:
dad
Output:
palindrome

Input:
Please insert a word:
hello
Output:
not a palindrome
========================
"""

x=raw_input('Please insert a word:')
 
#write your logic here


y=x[::-1] 
if x==y: 
	print('palindrome') 
else:
	print('not a palindrome') 
