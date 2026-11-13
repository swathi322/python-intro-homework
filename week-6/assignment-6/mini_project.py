numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
#1
def find_min(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for num in numbers:
      if num < min_value:
         min_value = num
    return min_value
#result_min_value = find_min(numbers)
#print(f"Returned minimum value from the list:  {result_min_value}")

#2
def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
      if num > max_value:
         max_value = num
    return max_value
#result_max_value = find_max(numbers)
#print(f"Returned maxmum value from the list:  {result_max_value}")

#3
def search(numbers, target):
    for i in range(len(numbers)):
     if numbers[i] == target:
       return i
    return -1
#search = int(input("Enter a number to search for: "))
#result = linear_search(numbers,search)

#if result != -1:  
#   print(f"Your serached number {search} is available in list at index value {result}.")
#else:
#   print(f"{search} was not found in the list.")

#4
def bubble_sort(data):
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    return data
#sorted_numbers = bubble_sort(numbers) # [3, 5, 8, 14, 17, 22, 29, 31, 40, 42, 47, 55, 59, 61, 66, 74, 78, 83, 86, 93]
#print(f"Please find the sorted numbers: {sorted_numbers}")

#5
def show_menu():
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    return int(input("pick an option (1 - 5): ").strip())
#6
def main():
    while True:
        choice = show_menu()

        if choice == 1:
         print(f"Returned minimum value from the list:  {find_min(numbers)}")
        elif choice == 2:
         print(f"Returned maxmum value from the list:  {find_max(numbers)}")
        elif choice == 3:
           target = int(input("Enter the number to search for: "))
           result = search(numbers, target)
           if result != -1:
            #print(f"found at index {index}")
            print(f"Your serached number {target} is available in list at index value {result}.")
           else:
            print(f"{target} was not found in the list.")
        elif choice == 4:
         print(f"sorted numbers' {bubble_sort(numbers)}")
        elif choice == 5 :
         print("Good bye!")
         break
        else:
         print("Invalid choice. try again.")

if __name__ == "__main__":
    main()