#Warmup 1: List Operations
#Create a hardcoded list of 8 numbers. Without using any loops, print:

#The first item
#The last item (use a negative index)
#A slice containing only the middle four items
#The full list in reverse order
#Example output (your numbers will differ):

#First:   42
#Last:    40
#Middle:  [83, 5, 61, 29]
#Reversed: [40, 86, 22, 59, 3, 78, 47, 14]

numbers = [10, 15, 20, 25, 30, 35, 40, 45]
print(numbers[0])
#print(f"Listed mumner {numbers}")
#print(f"The first item {numbers[0]}")
print(numbers[-1])
print(numbers[2:6])
numbers.reverse()
print(numbers)
