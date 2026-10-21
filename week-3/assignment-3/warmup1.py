#Warmup 1: Letter Grades
#Start with a hardcoded score variable (pick any number 0-100). Use if/elif/else to print the corresponding letter grade: 
#Score	Grade
#90-100	A
#80-89	B
#70-79	C
#60-69	D
#Below 60	F
#Example output:

#Score: 84
#Grade: B
#Save as: warmup1.py


#hardcoded score variable number(num) 0-100
score= int(input("enter a score "))
if score >= 90:
 print("grade A")
elif score >= 80:
 print("grade B")
elif score >= 70:
 print("grade C")
elif score >=60:
 print("grade D")
else:
 print("grade F")

 