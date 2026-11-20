#Warmup 1: Read a Text File Line by Line

with open("../data/notes.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"line {line_number} : {line.strip()}")   