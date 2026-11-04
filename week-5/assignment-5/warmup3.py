#Warmup 3: Linear Search

def linear_search(data, target):
    for i in range(len(data)):
     if data[i] == target:
            return i
    return -1

names = ["swathi", "varadhan", "dhanya", "marcus", "maddy"]
search = input("Enter a name to search for: ")

result = linear_search(names,search)

if result != -1:  
 print(f"Found {search} at index {result}.")
else:
 print(f"{search} was not found in the list.")