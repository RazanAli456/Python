#Write a Python program to find the sum and average of the list.
#The average of the list is defined as the sum of the elements divided by the number of the elements.
#Also, find the largest and the smallest number in the list.


sum=[20,34,45,67,89]
l=len(sum)
num=0
for i in range(0,l):
    num=num+sum[i]
print("Num =. ",num)

average=num/l
print("The Average Is", average)