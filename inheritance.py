
"""
Inheritence is a fundamental concept in object  oriented programming that allows(child class) to inherit attributes and the methods from another class.
This helps in using code and establishing in natural hierarchy between classes.
Class parent :Major class
  Parent class code 
class Child(parent): Minor class
  child class code

"""
# Single inheritance:
# Single inheritance occurs when a child class inherit from only one parent class. this is simplest form  of inheritance
# Syntax

class Parent:
    def parent_method(self):
        print("This is method of the parent class")
class Child(Parent):
    def child_method(self):
        print("This is method of the child class")
child=Child()
child.parent_method()
child.child_method()

#Example1
class Vehicle: #Parent class
    def __init__(self,make,model): #using constructor to give an attribute to be used by our object
        self.make=make #ceating attribute we shall assign values to 
        self.model=model
    def display_info(self): #this is parent class method
        print(f"Make:{self.make}, Model:{self.model}") #print statement
class Car(Vehicle): #child class
    def display_type(self): #constructor method to give attribute to be used in our objects
        print(f"{self.make} {self.model} is a car")
my_car=Car("One ten","Toyota") #creating an instance of car 
my_car.display_info() #using methods from parent class
my_car.display_type() #using methods from child class
