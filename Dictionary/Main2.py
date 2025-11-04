#Write a program to return the country code for various countries.
#  Here’s a dictionary of different country codes 
# - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.

CC={  
    "India":"0091",
    "Australia":"0025",
    "Nepal":"00977"
   }

print("The Country Code Of Japan Is", CC.get('Japan', 'not found') )

print("The Country Code Of Nepal Is", CC["Nepal"])