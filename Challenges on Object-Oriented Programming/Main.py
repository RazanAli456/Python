#Write a program to overload the less than (<) and equal to (==) operators.
#For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively.
#You can additionally create more objects to try different values.
class math:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if self.a<other.a:
            return("Obj1 Is Lesser Than Obj2")
        else:
            return("Obj2 Is Lesser Than Obj1")
    def __gt__(self,other1):
        if self.a>other1.a:
            return("Obj1 Is Greater Than Obj2")
        else:
            return("Obj2 Is Greater Than Obj1")
    def __eq__(self,other2):
        if self.a==other2.a:
            return("Obj1 And Obj3 Are Equal")
    def __add__(self,other3):
        return("obj1+obj2 Is " , self.a+other3.a)
obj1=math(6)
obj2=math(7)
obj3=math(6)
print(obj1<obj2)
print(obj1>obj2)
print(obj1==obj3)
print(obj1+obj2)