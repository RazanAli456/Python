#Write a Python program to create a class that will find the numbers in the tuple
#that add up to a sum and return the position of elements.
#The value of the sum can be taken as input from the user.
#Tuple - (10,20,30,40,50,60,70)

class numbers:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def rectangle_area(self):
        return self.l*self.w
obj1=numbers(10,20)
print("This Is The Area Of Rectangle", obj1.rectangle_area())

class square:
    def __init__(self,side):
        self.side=side
    def square_area(self):
        return self.side*self.side
obj1=square(60,70)
print("This Is The Area Of Square", obj1.square_area())