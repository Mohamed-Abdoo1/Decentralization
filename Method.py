

"""
Methods: in OOP method is a function that is defined with in a class and describes the behavior or actions that an object
can performe . methods defines how an object interact with it self and other objects , methods can be taken on from one
object to another. 
Attributes: these are variables that belong to an object . they define properties and characteristics of an object 
eg: name, age , size and etc.
"""

#Example1
#Methods contain the behavior of an object . they define what an objeect can do 
class Person: #This defines a new class called `Person`.
    def talk(self): #this define a method named `talk` within the `Person` class. 
        print("this girl speaks politely") #Thisoutputs the string `"this girl speaks politely"` 
person=Person() #This line creates an instance (object) of the `Person` class and assigns it to the variable `person`. 
person.talk() #This line calls the `talk` method on the `person` object and executes the code inside it `this girl speaks politely`.


#example2
class Car:
    def start(self):
        print("the car has started")
my_car=Car()
my_car.start()


#example4 class with multiple attributes
class Book:
    def _init_(self,title,author):
        self.title=title
        self.author=author
    def description(self): #it help us to print out a statement 
        print(f"{self.title}is written by{self.author}")
my_book=Book("Atomic Habit","Ahmed")
my_book.description()

#example3  class with an attribute and a method
class Dog:
    def _init_(self,name): #initializes the object attribute which help us to add objects
        self.name=name
    def bark(self):
            print(f"{self.name} is barking")
my_dog=Dog("Buddy")
my_dog.bark()

#Example5 : Modifying an attribute after creation
class Phone:
    def _init_(self,brand):
        self.brand=brand
    def call(self):
        print(f"Calling from {self.brand} phone")
my_phone=Phone("Apple")
my_phone.call()

my_phone.brand=("Samsung")
my_phone.call()