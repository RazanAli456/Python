#Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.
try:
    age=int(input("Enter Your Age Pls  : "))
    if age<0:
        print("The Age Can't Be Negative")
    elif age%2==0:
        print("Your Age Is A Even Number")
    elif age%2!=0:
        print("Your Age Is A Odd Number")
        
except Exception as e:
    print("Error ", e)
    