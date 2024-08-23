"""
Constructors are special method in python classes that automatically called when a new instance or a class is Created
they are used to initialize the atribute of new object ,.

KEY CONCEPTS:
1) __init__ method:
This method is called a constructor .
It is used to initialize an object atribute when the object is instantiated .
This method takes atleast one parameter :"self" which refers to the current instance to the class .

2) "self" parameter:
Self is reference to the instance of the class itself .
It allows access to the classes atribute and method.
While self is a conventional name it can technically been named anything, but using self is common practice .

3) Instantiation:
Creating  an instance of the class is called Instantiation.
During Instantiation , values are passed to the __init__method to initialize the object atribute .

4) 'pass' Statement: 
the 'pass' Statement is a place holder that does nothing .
It is used where code is syntatically required but not yet implemented .


"""
#Example one
class School:
    def __init__(self,name,location,teacher,student,motto):
        self.name = name
        self.location = location
        self.teacher = teacher
        self.student = student
        self.motto = motto
    def register(self):
        print(f"{self.name} is fully registered. ")
school1 = School("Caalami","Hargeisa","ina balayax", 425,"my country")
school2 = School("Irshad","Bur'o","ina seed", 543,"my country")
school1.register()
school2.register()

class Country:
    def __init__(self,name1,city,population):
        self.name1 = name1
        self.city = city
        self.population= population
    def country1(self):
        print(f"{self.city} in {self.name1} has {self.population} people")
country1 = Country("Somaliland","Hargeisa", 5.5)
country1.country1()


class Book:
    def __init__(self,title,Author):
        self.title=title
        self.Author=Author
    def description(self):
        print(f"{self.title} is written by {self.Author}")
book1=Book("Art of Laziness","Mohamed Cade")
book1.description()

class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print(f"{self.name} is barked")
dog=Dog("Cagacade")
dog.bark()

class Phone:
    def __init__(self,brand):
        self.brand=brand
    def call(self):
        print(f"{self.brand} is calling me ")
phone1=Phone("IPHONE")
phone1.call()

