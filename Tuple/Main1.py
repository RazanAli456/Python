#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not.
#  If it's a palindrome, then it is the same after being reversed.

front=(1,2,3,3,2,1)
back=front[::-1]
if front==back:
    print("It Is A Palindrome")
else:
    print("Its Not A Palindrome")