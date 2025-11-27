#Write a program to create a class with following variables and methods - 1.
#Private variable named privateVar that contains an integer value 2.
#Create a private function privMeth that prints a message 3.
#reate a function hello that prints the value of privateVar 4.
#Create an object for the class and call all the functions.
class R:
    __age=10
    def __Display(self):
        print("I Am Inside A Private Method")
    def hello(self):
        print(self.__age)
obj1=R()
obj1.hello()

