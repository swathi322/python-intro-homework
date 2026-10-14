#Write a script that contains a deliberate bug — for example, use a variable name that hasn't been defined, or forget to convert a string to an integer before doing math. Run it, read the error message, then fix the bug. Add a comment block describing:

#What the error message said (paste it)
#What caused it
#How you fixed it

#name=swathi
#age=31
#print("swathi you are 31 years old!)
#print(f"{name} you are {age}years old! ")

#Code line from 7to10, In my first run in above code I got below error
#SyntaxError: unterminated string literal (detected at line 9)

#name=swathi
#age=31
#print("swathi you are 31 years old!")
#print(f"{name} you are {age}years old! ")


#Code line from 15to18 :: Corrected the code with adding '"' in line 17, and did the second run in above code I got below error
# NameError: name 'swathi' is not defined (detected at line 15)

name="swathi"
age=31
print("swathi you are 31 years old!")
print(f"{name} you are {age}years old! ")

# Code line from 24to27 :: Corrected code line 24, name variable is string as I am using "Swathi", and did the third run and got the results without error

#Out put::
#swathi you are 31 years old!
#swathi you are 31years old!