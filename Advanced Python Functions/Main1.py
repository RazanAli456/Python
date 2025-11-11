#Write a program to return - 1.
#zipped list from two lists 2.
#elements of two lists zipped together, but 2nd list in reverse order 3.
#elements of two lists zipped into a dictionary

Name=["Razan","Sarim","Haris","Ajmal"]
Age=[10,9,10,10]
list1=zip(Name,Age)
list1=list(list1)
print(list1)
num1=[1,2,3,4]
num2=[5,6,7,8]
for a,b in zip(num1,num2[::-1]):
    print(a,b)