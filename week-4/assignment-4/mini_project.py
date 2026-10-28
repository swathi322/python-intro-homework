students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

#highest score and the name
top_scorer_name = ""
highest_score = 0
for student in students:
 if student["score"] > highest_score:
   highest_score = student["score"]
   top_scorer_name = student["name"]
print(f"Top scorer     :    {top_scorer_name} ({highest_score})")

#class average
total=0
for student in students:
    total += student["score"]
average = total/len(students)
print(f"Class_average  :    {average}")

#unique subjects
subjects = []
for student in students:
    subjects.append(student["subject"])
    unique_subjects = set(subjects)
#print(f"unique_subjects:    {subjects}")
print(f"Subjects offered:  {unique_subjects}")

#high scorers
high_scores = []
for student in students:
 if student["score"] >= 75:
     high_scores.append(student["name"])
print(f"High scorers   :    {high_scores}")



