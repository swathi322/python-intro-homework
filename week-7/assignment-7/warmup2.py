#Warmup 2: Read a CSV with DictReader

import csv
with open("../data/students.csv" , "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["score"])