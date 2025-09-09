#Write a program to show students' grades by entering five subject marks and calculating average marks and grades.
#For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?

math=float(input("Enter Your Marks"))
scince=float(input("Enter Your Marks"))
urdu=float(input("Enter Your Marks"))
english=float(input("Enter Your Marks"))
average=(math+english+urdu+scince)/4
if average>90 and average<100:
    print("Grade A1")
elif average>80 and average<90:
    print("Grade A2")
elif average>70 and average<80:
    print("Grade A3")
elif average>60 and average<70:
    print("Grade A4")
elif average>50 and average<60:
    print("Grade A5")
elif average>40 and average<50:
    print("Grade A6")
elif average>30 and average<40:
    print("Grade A7")
elif average>20 and average<30:
    print("Grade A8")
elif average>10 and average<20:
    print("Grade A9")
else:
    print("Grade A10")