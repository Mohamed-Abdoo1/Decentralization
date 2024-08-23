
"""
Exception handling in python is mechanism to handle runtime error so thet the normal flow of the application can be maintained 
it helps in dealing with errors gracefully with out crashing the program.

KEY CONCEPTS
1. Exception: is an event which occurs during execution of a program that  distrupt the nomal flow of the programs instruction.
2. Exception Handling: the process of  responding to the occurence of exception .

COMMON EXCEPTIONS:

A-> ZeroDivisionError: it is raised when division by zero is attempted.
B-> IndexError: it is raised when trying to access an element outside the list's range.
C-> KeyError: It is raised when dictionary key is not found .
D-> TypeError: it is raised when operation or function is applied to an object of inappropiate type.
E-> ValueError: it is raised when a function misused an argument of the right type but an inappropiate value.

"""# BASIC SYNTAX 
# try:
#     #code that might  araise an exception 
# except SomeException:
    #code to handle exception 
# Example1 (handling division by zero)


try:
    result=10/0
except ZeroDivisionError:
    print("You can't divide by zero")
#Example2 handling multiple eceptions 
try:
    A= int(input("Enter a number: "))
    B=int(input("Enter another number: "))
    result=A/B
except ValueError:
    print("Invalid input please enter numbers only")
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print(result)