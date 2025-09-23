#Write A Program To Find A Sum Of Normal Numbers

sum=0
n=int(input("Enter The Last Term "))
start=1
while start<=n:
    sum=sum+start
    start=start+1
print("Sum Is",sum)