 #Write a program to reverse the string entered by the user

word=input("Pls Enter A Word ")

lenght=len(word)-1
print("The Lenght Of The String Is",lenght)
for i in range(lenght,-1,-1):
    print(word[i] ,end="")