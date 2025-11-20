#Homework
class Dog:
    Specie="Dog"
    def __init__(self,age,name):
        self.age=age
        self.name=name
Brown=Dog(5,"Ben")
White=Dog(4,"Tom")
print("This Is My Brown Dog Name Is", Brown.name )
print("This Is My White Dog Age Is", White.age)