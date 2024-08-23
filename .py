

def odd(num1):
    for number in range(num1):
        if number % 2 != 0:
            print(number)
odd(7)


def square(number1):
    num = number1 * number1
    if num % 2 == 0:
        print("its even number number ")
    if num % 2 != 0:
        print("its Odd number")
square(6) 