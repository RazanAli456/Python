#Write a program to return the addition of numbers of two different lists.
#Then, display a list that is square of numbers of another list.
#Use the map() function here to get the desired result

num1=[11,45,67,23,98,87,54]
num2=[22,90,76,46,89,64,69]
num3=map(lambda a,b:a+b,num1,num2)
num3=list(num3)
print(num3)
num4=[4,5,6]
num5=map(lambda x:x**2,num4)
num5=list(num5)
print(num5)