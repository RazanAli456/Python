#First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
about={
      "Name":"Razan",
      "Age":10,
      "Class":4,
      "School ID":"20-0907",
      "School":"Bravian School",
      "Favourite Subject":"Math"

     }
print("The Name Of The Student Is", about["Name"])
print("The Student Favourite Subject Is ", about["Favourite Subject"])

for key,value in about.items():
    print("The Key Is", key)
    print("The Value Is", value)