import turtle
def well_wishes(name):
    print("We Are Learning Functions By "+name)
name=("Razan")
well_wishes(name)

#Write a program to display the weather in autumn and spring
print("Which Season You Want To Learn About?Autumn Or Spring")
choice=input("")
def spring():
    print("Spring is a season of new beginnings that follows winter and precedes summer, characterized by gradually rising temperatures, longer days, and the blooming of flowers and new leaves on trees")
def autumn():
    print("Autumn is the season transitioning from summer to winter, marked by cooler temperatures, shorter days, and visible changes in nature like colorful leaves on deciduous trees falling to the ground")
if choice=="autumn":
    autumn()
else :
    spring()