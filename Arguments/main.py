#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
def total_calc(amt,tip=1):
    tip_amt=(tip/100)*amt
    total=amt+tip_amt
    print("Your Total Bill Is",total)
amt=float(input("Enter The Your Bill"))
tip=float(input("How Much Percent You Will Give As A Tip"))

total_calc(amt,tip)