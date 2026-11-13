def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    return data
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
sorted_numbers = bubble_sort(numbers) # [3, 5, 8, 14, 17, 22, 29, 31, 40, 42, 47, 55, 59, 61, 66, 74, 78, 83, 86, 93]
#print(bubble_sort(numbers))
print(sorted_numbers)

while True:
  print("=== Number Cruncher ===")
  print("1. Find minimum")
  print("2. Find maximum")
  print("3. Search for a number")
  print("4. Sort the list")
  print("5. Quit")

  choice = int(input("pick an option (1 - 5): ").strip())
  
  if choice == 1:
    if not numbers:
      print("The list is empty")
    else:
      mini_value = numbers[0]
      for num in numbers:
        if num < mini_value:
          mini_value = num  
      print(f"Minimum value from the list is: {mini_value}")
  elif choice == 2:
    if not numbers:
      print("The list is empty")
    else:
      max_value = numbers[0]
      for num in numbers:
        if num > max_value:
          max_value = num  
      print(f"Maximum value from the list is: {max_value} ")

  elif choice == 3:
      print("The list is empty.")
    else:
      min_value = numbers[0]
      for num in numbers:
        if num < min_value:
          min_value = num

    print(f"Minimum value from the list is: {min_value} ")

  elif choice == 2:
   if not numbers:
    print("The list is empty")
   else:
    max_value = numbers[0]
    for num in numbers:
      if num > max_value:
        max_value = num
    print(f"Maximum value from the list is: {max_value} ")

  elif choice == 3: 
    def linear_search(data, target):
      for i in range(len(data)):
       if data[i] == target:
         return i
      return -1
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
    search = int(input("Enter a number to search for: "))

    result = linear_search(numbers,search)

    if result != -1:  
      print(f"Your serached number {search} is available in list at index value {result}.")
    else:
      print(f"{search} was not found in the list.")
  elif choice == 4:
    print(sorted_numbers)
  elif choice == 5:
    print("Good Bye")
    break
  else:
    print("Invalid choice, please try again.")