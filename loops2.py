
"""
While loop repeatedly executes a block of code as long as specified condition is true .
"""
#Example 01 Counting with while loop
def even():
    num1 = 0 #Variable that stores values
    while num1  <= 100: #checks whether condition is equal or less then 100
        print(num1)
        num1 += 10 #adds 10 each result until reaches 100,adds 10 to make it 20 and so on 
even()

#Example 02 Counting odd numbers with while loop
def odd():
    num2 = 1
    while num2 <= 100:
        print(num2)
        num2 += 10
odd()

#KEY POINTS TO REMEMBER

"""
For Loops is used for iterative over sequence where as while loop is used to repeating block of code 
as long as condition is true 
"""
