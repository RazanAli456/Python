#Write a program to understand how the value error exception works?
try:
    num=int(input("Pls Enter A Number :"))
    print(num)
except ValueError as e:
    print("Value Error:", e)