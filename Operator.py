#Arithmetic operator (+,-,/,*,%,**,//,=)
"""
+ Addition sign
- subtraction
* Multiplication
/ Division
% Modula sign
** Power
// floor division
"""
#Example how arithmatic operators are used

"""
number_1 = 5
number_2 = 6
print(number_1 + number_2)


number_1 = 5
number_2 = 6
print(number_1 - number_2)


number_1 = 5
number_2 = 6
print(number_1 * number_2)


number_1 = 5
number_2 = 6
print(number_1 / number_2)


number_1 = 5
number_2 = 6
print(number_1 % number_2)


number_1 = 5
number_2 = 6
print(number_1 ** number_2)


number_1 = 5
number_2 = 6
print(number_1 // number_2)
"""





#Assignment Operator
"""
= Assigment operator
+= Addition assigment operator
-= Subtraction assigment 
*= Multiplication assignment
/= Division Assignment
%= Remainder Assignment
**= Exponent Assignment

#Example how assignment operators are used
A = 10
A += 8 
print(A)
B = 12
B -= 8 
print(B)
C = 10
C *= 8 
print(C)
D = 18
D /= 9 
print(D)
E = 10
E %= 3 
print(E)
F = 10
F **= 5 
print(F)

"""

#comparison Operators
"""
== is Equal to
!= Not Equal to
> Greater than
< Less than
>= Greather than or equal to
<= Less than or equal to


#Examples 
Num1 = 3
Num2 = 5
print(Num1 == Num2)
print(Num1 != Num2)
print(Num1 > Num2)
print(Num1 < Num2)
print(Num1 >= Num2)
print(Num1 <= Num2)
"""

#LOGICAL OPERATORS
"""
Logical operators are used to check whether an expression is true or false ( used for decision marking)
AND 
OR
NOT

print(True and True)
print(True and False)
print(True or True)
print(not True)

"""
#MEMBERSHIP OPERATORS
"""
Membership operators are used to test if a sequence is presented in an object Or not:
There are two operators that undergoes Membership operator and they are :-
IN ( it returns true if the object is present in the sequence)
NOT IN ( it returns true if the object is not present in the sequence)
"""
#Example
clothes = ["t-shirt", "Shirt", "Pants"]
print("Shirt" in clothes)
language = ["English","Arabic","Kiswahili"]
print("french" not in language)

#BITWISE OPERATOR
"""
Bitwise operators are used to compare (binary) numbers and they are:-
& AND  (Sets 1 if both bit are 1)
| OR   (Sets 1 if one of two(bits) are 1)
^ BITWISE EXCLUSIVE OR (Sets 1 if only one of two is 1)
~ NOT BITWISE (inverts all the bits)
<< LEFT SHIFT (The left shift operator shifts all bits in a number to the left by a specified number of positions)
>> RIGHT SHIFT (The right shift operator shifts all bits in a number to the right by a specified number of positions)
"""
#Example
print( 7 & 2 )
print( 7 | 2 )
print( 7 ^ 2 )
print(~ 5 )
print( 4 << 2 )
print( 4 >> 2 )

