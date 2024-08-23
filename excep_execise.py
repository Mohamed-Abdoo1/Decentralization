
def divide(a, b):
    if b == 0:
        raise ValueError("The divisor cannot be zero.")
    return a / b

# Exception Handling
try:
    result = divide(10, 0)
except ValueError as e:
    print(e)  # This will print: The divisor cannot be zero.
   def divide(a, b):
       if b == 0:
           raise ValueError("You cannot divide by zero!")
       return a / b

   try:
       result = divide(10, 0)
   except ValueError as e:
       print(e)  # This will print: You cannot divide by zero!

