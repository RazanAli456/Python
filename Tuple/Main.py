#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
num=("Razan",9,25.5,True,)
print(type(num))
num1=(1,1,1,2,3,4,5,6,7,8,9)
print((num1))
num1=num1+(10,11)
print(num1)
print("The Number Of Times 1 Occurs: ", num1.count(1))
print(num1[3:6])