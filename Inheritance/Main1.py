#Write a program to create a parent class Person
#(attributes - name, id number) with a method display to display the attributes
# Next, create a child class Employee (attributes - name, id number, salary, post).
#Access the attributes of parent class in child class. Then,
#create an object for child class and call the display method to display the name
#and id number.

class Person:
    def __init__(self,Name,ID_Number):
        self.Name=Name
        self.ID_Number=ID_Number
    def display(self):
        print("The Person Name Is ", self.Name)
        print("The ID_Number Is " , self.ID_Number)
class Employee(Person):
    def __init__(self,Name,ID_Number,salary,post):
        Person.__init__(self,Name,ID_Number)
        self.salary=salary
        self.post=post
obj1=Employee("Razan",200907,100000,"BOSS")
obj1.display()
print("The Salary Is", obj1.salary)
print("The Post Is" , obj1.post)