#Write a Python program to implement Inheritance by creating a Parent
#Class Vehicle with a constructor
#that has details like name,
#maximum speed, and mileage.
#Then, create a Child Class Bus that inherits Class Vehicle
#.Finally, showcase Inheritance to display the details of the Vehicle Bus named
#- School Volvo.

class Vehicle:
    def __init__(self,Name,MaximumSpeed,Millage):

        self.MaximumSpeed=MaximumSpeed
        self.Millage=Millage
        self.Name=Name
class Bus(Vehicle):
    pass
obj1=Bus("Volvo",200,5)
print("The Name Of The Bus Is", obj1.Name)
print("Vehicle Speed", obj1.MaximumSpeed)
print("Vehicle Millage", obj1.Millage)
