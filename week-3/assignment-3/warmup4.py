number=int(input("Enter a numbrer "))
if number<0 and number%2!=0:
 print(f"Enter a number: {number}")
 print(f"{number} is negative.")
 print(f"{number} is odd.")
elif number<0 and number%2==0:
 print(f"Entered number: {number}")
 print(f"{number} is nagative.")
 print(f"{number} is even.")
elif number>0 and number%2!=0:
 print(f"Enter a number:{number}")
 print(f"{number} is positive.")
 print(f"{number} is odd")
elif number>0 and number%2==0:
 print(f"Enter a number:{number}")
 print(f"{number} is positive.")
 print(f"{number} is even")
else:
 print(f"Enter a number:{number}")
 print(f"{number} is zero ")
 print(f"{number} is even")