#Write a program to check how the exceptions and finally statement works
try:
    num1,num2=eval(input("Enter Two Numbers Seperated By A Comma  : "))
    num3=num1/num2
    print(num3)
except SyntaxError as s:
    print("Error", s)
except ZeroDivisionError as e:
    print(e)
except  ValueError as v:
    print(v)
finally :
    print("The Code Is Good")
