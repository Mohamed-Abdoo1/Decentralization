"""
Data types are used to define type of data,variable or object can hold and how the computer
system should interpret it is value
Categorization of values that are going to be stored a variable names prevents computer
memory wastage
EXAMPLES OF DIFFERENT DATA TYPE
NUMERIC DATATYPE
STRING 
SEQUENCE OR LIST
MAPPING(DICT)
BOOLEANS
SET
"""
#EXAMPLES OF NUMERIC DATATYPE
"""
INT (Whole Number)
FlOAT (Decimal Number)
COMPLEX
"""
Num1 = 1000
Num2 = 100.3
Num3 = 1+2j
Num4 = "1000"
print(type(Num1))
print(type(Num2))
print(type(Num3))
print(type(Num4))

"""
STRING DATATYPE (str)
Any value is single or double qoutes is string.
"""
#Examples
name = "Nabi ku sali"
print(type(name))

"""
SEQUENCE/LIST 
This refers to ordered list of elements or terms
this elements can be numbers,characters or any other datatype and they follow specific order .
"""
#Example
my_list = [0,2,4,6]
print(type(my_list))
my_list2 = [0,2,4,6,"Nabi ku sali",0.5]
print(type(my_list2))

"""
TUPLE 
It serves as an ordered collection of elements often used for grouping related data .
NOTE tuples are immutable in python meaning their elements can not changed after creation

"""
#Example
my_tuple = (0,2,4,6)
print(type(my_tuple))

"""
Mapping (dict)
Dictionary is built in mapping type that consist of collection of key value pairs.
"""
#Example
my_dict = {"Somaliland":"Hargeisa","Uganda":"Kampala","kenya": "Nairobi"}
print(type(my_dict))
"""
Booleans always denoted True and false. They are designed to represent the two truth values
"""

#Example
name1 = True
name2 = False
print(type(name1))
print(type(name2))

"""
Sets Gives you unordered list of items 
NOTE it eliminates duplicate items
"""
#Example
my_set = {2,4,6,8}
my_set2 = {3,3,5,7,7,9}
print(my_set)
print(my_set2)
print(my_dict)