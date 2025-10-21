#RazanTheBest Guy :D.He Is The Best!Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan Razan 
import random

computer_guess=random.randint(1,20)

tries=0

while tries<5:
    UserChoice=int (input("Enter Your Choice"))
    tries=tries+1
    if UserChoice==computer_guess:
        print("You Have Guessed The Right Number In These Many tries", tries)
    elif UserChoice<computer_guess:
        print("Guess Higher")
    elif UserChoice>computer_guess:
        print("Guess Lower ")