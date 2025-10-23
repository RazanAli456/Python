#Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip.

def flight_cost(city):
    if city=="islmabad":
        flight_cost=5000
    elif city=="lahore":
        flight_cost=7000
    elif city=="karachi":
        flight_cost=10000
    return flight_cost
def car_rent(days):
    if days>7:
        car_rent=100*days
    else:
        car_rent=80*days
    return car_rent
def hotel_cost(days):
    if days>1:
        cost=100*days
    return cost
city=input("Which City You Wanna Go?")
days=int(input("How Many Days You Wanna Go For?"))
fc=flight_cost(city)
cr=car_rent(days)
hc=hotel_cost(days)

total=fc+cr+hc
print("Total Cost Of The Trip Is ", total)