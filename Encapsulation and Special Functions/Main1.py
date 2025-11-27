#Write a program to create a class Computer with a private attribute
#max_price and methods sell(to display) the selling price and setmaxprice
#(change the private attribute max_price). Now create an object for the class Computer.
#Try changing the value of max price and use the sell function to display the updated price
#Use a setter function to update the value and again display the price.Project:

class Computer:
    __MaxPrice=2000
    def sell(self):
        print("The Maximum Price Is" , self.__MaxPrice)
    def setmaxprice(self,Price):
        self.__MaxPrice=Price
obj1=Computer()
obj1.setmaxprice(3000)
obj1.sell()