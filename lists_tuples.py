"""
Lists are mutable data structure that can store multiple values
values in alist are accessed used indaces starting from 0
Negative indaces can be used to access values from the end of the list for example negative 1(-1) from the last item
"""
#Example
my_list = [0,1,2,3,4,5,6,7,8,9] #An Example of nonnested list
print(my_list[5])
print(my_list[9])
print(my_list[-1]) #9 is in position -1 from right 

#Example two
num1 = [100,[200]] #An EXample of Nested Lists
print(num1[0])
print(num1[-1][-1])
print(num1[-2])
print(num1[1][0])


"""
Nonnested lists are simple lists that contain a series of elements which can be any data type (integer,sing,float and etc)
but do not contain other lists as elements .

Nested lists that contain other lists as their elements 
"""

#Tuples 
"""
A tuple is immutable we can access values that we can not add or remove anay thing
We access values as same way we access vaues in lists
"""
#Example 
my_tuple = (10,20,30,40,50)
print(my_tuple[2])

#How to add,remove,delete items in list
we_list = [0,2,4,8]
we_list.append(10) #This helps to add value on list
print(we_list)

we_list.pop() #This deletes values begining with the last value in list
print(we_list)


we_list.remove(0) #This removes a specific item in list
print(we_list)

fruits = ["Banana","Apple","Mango"]
fruits.append("Lemon")
print(fruits)


#Dictionaries
"""
its identified by braces {}
we can add or remove anything
to see indices or keys we use dot keys (. keys())
To see Values we used dot values (. values())
"""
#Example
My_dict = {"Somalia":"Mogadisho", "Khaatumo":"Laaska", "kenya":"Nairobi"}
print(My_dict.keys())
print(My_dict.values())

My_dict.__delitem__("Khaatumo")
print(My_dict)



