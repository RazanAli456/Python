#Write a program to create a set and perform the following operations on that set- 1.
#  Create a set with integer elements 2.
#  Create a set with mixed data type elements 3.
#  Create another set with elements - 1, 2, 3, 4, 3, 2 4.
#  Create a set from a list with elements - [1, 2, 3, 2] 5.
#  Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
NUM={1,1,1,2,3,3,3,4,5,6,7,8,8,8}
print(NUM)
NUM1={True,67.67,"Razan",67,10,1234567890}
print(NUM1)
NUM2=[1,3,8,4,2,6,5,9,7,0,1,2,3,4,1,4,9,8]
NUM2=set(NUM2)
print(NUM2)
NUM3={1,2,3,4,5,6,7,8}
NUM3.add(9)
print(NUM3)