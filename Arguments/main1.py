#Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(num):
    if num%3==0:
        print("The cube of the number is",num**3)
    else:
        print("This Number Is Not divisible By 3")
num=int(input("Pls Enter A Number"))
cube(num)