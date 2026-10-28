#Warmup 2: Dictionary Operations

student = {"name" : "Varadhan", "grade" : "A+", "subjects" : ["math","science"]}
for key, value in student.items():
 print(f"{key} : {value}")
student["graduated"] = False
print(list(student.items()))

