
#Dynamic functions with parameters allow us to create functions that accept input values known us parameters when they are called .
# These parameters provides function with the neccesary to perfom its test to perform its test Making the function more versatile and reusable.
# Two types of function Static Function And Dynamic so now lets deal with dynamic Function

#Example 1
def add(num1,num2 ): #inside the define function we have parameters or arguments .
    num3 = num1 + num2 
    print(num3)
add(8,7) # These are values

def modd(num1,num2 ):
    num3 = num1%num2 
    print(num3)
modd(8,3)

def sub(num1,num2):
    num3 = num1-num2 
    print(num3)
sub(15,10)
sub(7,7)

def multi(num1,num2):
    num3 = num1*num2 
    print(num3)
multi(5,5)

def div(num1,num2):
    num3 = num1/num2
    print(num3)
div(10,2)

def expo(num1,num2):
    num3 = num1**num2
    print(num3)
expo(5,2)