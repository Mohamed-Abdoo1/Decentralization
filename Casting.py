
"""
Type casting is process of converting a value from one data type to another.
common type casting functions include 
int() this converts value to an integer.
Float() this converts value to float.
str() this converts the value to string.
list() this converts value to list.
tuple() this converts value to tuple
"""
#Example 1
num_str = "123"
num_int = int(num_str)
print(num_int)

Num_str = "123.5"
Num_float = float(Num_str)
print(Num_float)

Num = 123
Num_str = str(Num)
print(Num_str)

list = [1,2,3,4]
tuple = tuple(list)
print(tuple)

"""
Remember that input() in python 3 returns a string 
Convert when its neccessary : use type casting to convert input of require data type before performing operation .
"""
