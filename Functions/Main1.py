#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.

num1=int(input("Enter First Number"))
num2=int(input("Enter Second Number"))
operater=input("Enter Operator (+, -, *, /) : ")
def add(a,b):
    print("The Sum Is",a+b)
def minus(a,b):
    print("The Subtraction Is",a-b)
def multiply(a,b):
    print("The Mulitplication Is",a*b)
def divide(a,b):
    print("The Division Is",a/b)

if operater=="+":
    add(num1,num2)
elif operater=="-":
    subtract(num1,num2)
elif operater=="*":
    multiply(num1,num2)
else:
    divide(num1,num2)
