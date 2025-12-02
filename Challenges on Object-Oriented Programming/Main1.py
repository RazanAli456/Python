#Write a program to create a quiz related to multiple fruits using object-oriented programming 
#in Python. Create a class that consists of - 1. 
#a constructor with a dictionary of fruits and respective colours 2. 
#a function to execute the quiz. 
#Here, the fruit will be chosen at random from the dictionary.
#Then ask the user to enter the colour of that fruit.
#Evaluate the answer and display the result accordingly.

class FruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}
    def quiz(self):
        for f,c in self.fruits.items():
            print("What Is The Color Of The" ,f)
            ans=input("Enter Your Answer ")
            if ans==c:
                print("Correct")
            else:
                print("Incorrect")
obj1=FruitQuiz()
obj1.quiz()
