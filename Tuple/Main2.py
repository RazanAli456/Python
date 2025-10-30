#Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0).
#If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1.
#On the basis of the value of rainy and sunny, predict the weather.

weather=(1, 0, 0, 1, 1, 0)
rainy=0
sunny=0
for i in weather:
    if i==1:
        rainy=rainy+1
    else:
        sunny=sunny+1
print("The number of rainy days are:",rainy)
print("The number of sunny days are:",sunny)
