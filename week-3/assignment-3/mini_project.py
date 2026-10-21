day= input("Enter a day ").lower()
time = input("Enter a time ").lower()
if day == "monday" and time == "morning":
 print("Morning python class, great time to focus")
elif day =="monday" and time == "afternoon":
 print("Have a Lunch")
elif day == "monday" and time =="evening":
 print("Go for a walk")
elif day == "thursday" and time == "morning":
 print("breakfast time")
elif day == "thursday" and time == "afternoon":
 print("Attend a python group session ")
elif day == "thursday" and time == "evening":
 print("it's time to relax ")
elif day == "sunday" and time == "morning":
 print("Try some new receipes")
elif day == "sunday" and time == "afternoon":
 print("Enjoy outing with kids")
elif day == "sunday" and time == "evening":
 print("Movie time")
else:
 print("Sorry, I don't recognize that day. Try: Monday, Thursday, Sunday")
