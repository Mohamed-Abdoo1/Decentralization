
#We can group code relatable to each other and give it name .
# A group of statements relatable to each other is a function .
"""
To define a function in python we use "def" keyword followed by the function name and pair of
parentheses 
"""
#Example One
def sum():
    print("Testing our code")
    num1,num2 = 4,6
    num3 = num1 + num2
    print(num3)

sum()
# To execute this block of code we are supposed our function or invoke 
# Example Two
def sub():
    n1,n2 = 8,6
    n3 = n1 - n2
    print(n3)
sub()

def div():
    num1,num2 = 10,2
    num3 = num1/num2
    print(num3)
div()

def expo():
    num1,num2=5,2
    num3=num1**num2
    print(num3)
expo()
