#Write a program to create a class Parrot and perform the following tasks - 1.
#Create a class variable species 2.
#Create a __init__ method that has instance variables - name and age 3.
#Create instances of class Parrot, passing arguments as well 4
#Print Class variable by accessing it 5
# Print Instance variables as well

class parrot:
    Specie="Bird"
    def __init__(self,age,name):
        self.age=age
        self.name=name
Blue=parrot(5,"Ben")
Green=parrot(4,"Tom")
print("This Is My Blue Parrot", Blue.name )
print("This Is My Green Parrot", Green.age)