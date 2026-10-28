#Warmup 3: Set Operations
#Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:

#The union (all languages from both lists, no duplicates)
#The intersection (languages in both lists)
#The difference (languages only in the first list)

set_a = {"python", "javascript", "java", "typescript"}
set_b = {"c++", "c#", "typescript", "java"}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))