#Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3].
#Then find the number of occurrences of number 3 in the array. Also, print the reversed array

import array as a
NUM=a.array('i',[1, 3, 5, 3, 7, 9, 3])
print("The array Of INT Numbers Is", NUM)
NUM1=a.array('d',[1.45,67.67,98.1,99.9])
print(NUM1)
print("How Many Number 3 Is In The Variable NUM???", NUM.count(3))
NUM.reverse()
print("The Reverse NUM is", NUM )