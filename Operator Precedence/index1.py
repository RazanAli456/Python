#Write to check a number is divisible by another number.

a=int(input("Pls Enter A Numerator "))
b=int(input("Pls Enter A Denomenator "))

if b==0:
    print("Denomenator Can't Be Zero. ")
    b=int(input("Pls Enter Another Denomenator :"))

print(str(a)+"is divisible by ",str(b))