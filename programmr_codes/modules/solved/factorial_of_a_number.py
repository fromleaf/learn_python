"""
Write a programe which prints the factorial of a given number?

=====================
Input:
Enter the number:
0
Output
1

Input:
Enter the number:
3
Output:
6

=====================
"""

n=int(input("Enter the number:"))

#write logic here
result = 1
for i in range(1, n+1):
	result = result * i
print(result)
	
