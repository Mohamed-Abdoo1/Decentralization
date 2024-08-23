"""
Multiple inheritence allows a class to inherit for more than one parent class. this can be useful when you want to combine features from multiple classes.

"""
#SYNTAX 
class Parent1:
    def method1(self):
        print("method from parent1")

class Parent2:
    def method2(self):
        print("method from parent2")

class Child(Parent1,Parent2):
    def child_method(self):
        print("method from child class")

child=Child()
child.method1()
child.method2()
child.child_method()

#example1
class Person: #class parent one
    def __init__(self,name,age): 
        self.name=name
        self.age=age
    def display_personal_info(self):
        print(f"Name{self.name},Age: {self.age}")

class Job: #class parent two
    def __init__(self,job_title,salary):
        self.job_title=job_title
        self.salary=salary
    def display_job_info(self):
        print(f"Job title:{self.job_title},Salary:{self.salary}")

class Employee(Person,Job): #class child inheriting from both parent class one and two
    def __init__(self,name,age,job_title,salary,employee_id):
        Person.__init__(self,name,age)
        Job.__init__(self,job_title,salary)
        self.employee_id=employee_id
    def display_employee_info(self):
        self.display_personal_info()
        self.display_job_info()
        print(f"Employee Id :{self.employee_id}")

employee=Employee(" Mohamed",  55, " CEO", 17000," C112")
employee.display_employee_info()

