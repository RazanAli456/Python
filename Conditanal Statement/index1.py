#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?
cp=float(input("Cost Price Of Orange"))
sp=float(input("Enter Selling Price Of Orange "))
if sp>cp:
    print("You Got A Profit Of", sp-cp)
else :
    print("You Have Lost Some Money", cp-sp)
