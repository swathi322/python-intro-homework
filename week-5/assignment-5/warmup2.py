#Warmup 2: Input Validation with a While Loop
while True:
 input_value = input("Enter a positive integer: ")
 if input_value.isdigit() and int(input_value)>0:
  print(f"Got it: {input_value}")
  break
 else:
  print("That's not a positive integer. Try again.")


 