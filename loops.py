
"""
A loop is an instruction that tells the computer to repeat performance of certain task.
It's purpose is to execute block of code multiple times untill specified condition just met 

TYPES OF LOOPS:-
FOR LOOP
WHILE LOOP
DO WHILE LOOP (CONT COMMON OR APPLICABLE)
"""
#EXAMPLE 1 Counting with a loop
"""
For loop iterates over a sequence (like a list,tuple,string or range  ) And execute a block of code for Each element in sequence. 
"""
def my_count():
    for item in range(10): #For function it initiates the loop then Item is variable that takes on each value in the sequence one at a time. 
        print(item)
my_count()

#Example 2 Accessing list element with a loop
def list():
    lang = ["Python","javascript", "c","Ruby","Swift"]
    for langs in lang:
        print(langs)
list()

#Example 3 Using for loop with a parameter
def parameter(num):
    for number in range(num):
        print(number)
parameter(5)

#Example 4 Conditional statement inside for loops
def my_lang():
    haye = ["Pyth","java", "c#","Swift"]
    for hayedee in haye:
        if hayedee == "java":
            print("You are currently in java class")
my_lang()

#Example 5 Finding Even number with loop
def even(num1):
    for numbers in range(num1):
        if numbers % 2 == 0:
            print(numbers)
even(8)

