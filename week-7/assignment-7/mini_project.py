import os
import csv
print(os.getcwd())

input_path = "../data/expenses.csv"

#Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
if not os.path.exists(input_path):
    print("File not found")    
else:
    print("File is available.")

#Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.

with open(input_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['date'], row['category'],row['description'],row['amount'])

#Convert the amount field to float for each row.
price = float(row['amount'])
with open(input_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['date'], row['category'],row['description'],{price})

#Filter the list to only rows where category is "Food".
with open(input_path, 'r') as file:
    records = list(csv.DictReader(file))
for item in records:
    item['amount'] = float(item['amount'])

food_items = [item for item in records if item['category'] == 'Food']
print(food_items)

#Calculate the total amount spent on Food.
#food_value = sum(item['amount'] for item in records)
food_value = sum(item['amount'] for item in food_items)
print(f"Total amount spent on Food: ${food_value:.2f}")

#Write a report to food_report.txt with this structure
from datetime import datetime
now = datetime.now()
print(f"Today is {now.strftime("%B %d, %Y")}")
#One line per food expense: [date]: $[amount]

#One line per food expense: [date]: $[amount]
with open("output.txt", "w")as file:
 for item in food_items:
    file.write(f"{item ['date']}: ${item['amount']:.2f}\n")

#Last line: Total: $[total to 2 decimal places]
#item['amount'] = float(item['amount'])
total_spent = sum(item['amount'] for item in value)
print(f"Total:${total:.2f}")
