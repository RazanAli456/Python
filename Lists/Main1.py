#Write a program to perform the following operations  on a List: 1. 
# Create an empty list 2. A list with elements 
# 3. Use * operator 4
# . Reverse a list

Name=[]
print("The Data Type Of The Variable Name Is", type(Name))

AboutMe=["Razan",10,"Gamer And Coder",True,24.8]
print("My Age Is ", AboutMe[1])
print("My Weight Is", AboutMe[4])
print("I Am A", AboutMe[2])
print("My Name Is", AboutMe[0])
print("Am I A Student?",AboutMe[3])
AboutMe.append("I Am From Bravian International School")
print(AboutMe)
AboutMe.pop()
print(AboutMe)
list1=[4,5,6]
num=list1*3
print(num)
list1.reverse()
print(list1)
l=len(list1)
print("The Number Of Elemants",l)