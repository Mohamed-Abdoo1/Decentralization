
"""
in python 3 input () is function that is used to capture user input from the keyboard.
it always returns the input as a string 
"""
#Example 1
user_input = input ("ENTER ANYTHING :")
print("You have entered :", user_input)

"""
Since input return as string, you need to convert the input the other data type (integer or float) as needed .
"""
#Example 2
Age = input ("Enter Your Age :")
print("Your age as string:", Age)

Age_int = int(Age)
print("Your Age as integer", Age_int)

#Example 3
name = input("Enter Your Name :")
print("Hello " + name + "!")

