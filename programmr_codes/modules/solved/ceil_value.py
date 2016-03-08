"""
Write a code which prints the Ceil value of a floating point number
Input:
Enter the number:
5.9
Output:
6

Input:
Enterthe number:
3.1
Output:
4
"""
x = float(raw_input('Enter the Number:')) 
 
#write logic here
split_num = str(x).split(".")
print(split_num[0])
ceil_num = int(split_num[0]) + 1
print("Output:")
print(ceil_num)


split_num = str(x).split(".")

if 0 <= int(split_num[1]) < 5:
	ceil_value = int(split_num[0])
else:
	ceil_value = int(split_num[0]) + 1
		    
print("Output:")
print(ceil_value)
