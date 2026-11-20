import csv
from datetime import datetime
import os

input_path = "../data/expenses.csv"
output_path = "food_report.txt"
file_path = "my_file.txt"

#Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
if not os.path.exists(file_path):
    print("File not found")
   # print(f"Error: the file{file_path} does not exists.")

 #Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.

expenses =[]
with open(input_path, mode="r", newline="", encoding="utf-8") as file:
   reader = csv.DictReader(file)
for raw in reader:
  print(raw)
#Convert the amount field to float for each row.

row["amount"] = float(row["amount"])
expenses.append(row)

#filter the list to only rows where category is "Food".
food_expenses = [row for row in expenses if row["category"] == "food"]

#Calculate the total amount spent on Food
total_food = sum(row["amount"] for row in food_expenses)

#Write a report to food_report.txt with this structure
today_str = datetime.now().strftime("%B %d, %Y")

with open("food_report.txt", mode="w", encoding="utf-8") as report:
    report.write(f"Food expenses report - generated {today_str}\n")
    for item in food_expenses:
        report.write("f{item['date']}: ${item['amount']:.2f}\n")
    report.write(f"Total:${total_food:.2f}\n")
print("generated reporti in food_report.txt.")