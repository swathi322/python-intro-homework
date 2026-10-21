#Write a program that asks the user for a day of the week and a time of day (morning, afternoon, or evening), then suggests an activity.
#Requirements:
#Cover at least 3 days × 3 times = 9 combinations with distinct suggestions
#Handle any unrecognized day or time with a friendly fallback message
#Normalize input so capitalization doesn't matter (e.g., "Monday" and "monday" both work)
#Example output (the suggestion and fallback wording are your own — any sensible messages are fine):

#What day is it? Tuesday
#What time of day? morning
#Suggestion: Morning Python class — great time to focus!

#What day is it? Saturday
#What time of day? evening
#Suggestion: Perfect night for a movie or trying a new recipe.
#What day is it? blah
#What time of day? morning
#Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...s

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
 print("Sorry, I don't recognize that day. Try: Monday, Thursday, Sunday...")
