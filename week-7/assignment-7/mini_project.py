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
food_value = sum(item['amount'] for item in food_items)
print(f"Total amount spent on Food: ${food_value:.2f}")

#First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
from datetime import datetime
now = datetime.now()
current_date = now.strftime("%B %d, %Y")
print(f"Food Expense Report — generated: {current_date}")
