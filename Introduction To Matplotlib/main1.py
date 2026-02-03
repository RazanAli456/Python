import matplotlib.pyplot as plt
import numpy as np
student_name=["Razan","Faizan","Sarim","Zaviyan","Neon"]
student_marks=[50,50,45,50,50]
student_perc=[]
for i in student_marks:
    p=i/50*100
    student_perc.append(p)
print(student_perc)
plt.plot(student_name,student_marks)
plt.title("Student Percentage")
plt.xlabel(student_name)
plt.ylabel(student_marks)
plt.show()

plt.plot(student_name,student_perc)
plt.title("Students Name And Percentage")
plt.xlabel(student_name)
plt.ylabel(student_perc)
plt.show()