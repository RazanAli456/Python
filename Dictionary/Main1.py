#Write a program to check the frequency of a value in a dictionary 
# - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
Condingal={
        'Codingal' : 2,
         'is' : 2,
         'best' : 2,
         'for' : 2,
         'Coding' : 1
          }
count=0
for key,value in Condingal.items():
    if value==2:
        count=count+1
print("The Number Of Times 2 Is Repeated Is", count)