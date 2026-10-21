#Warmup 3: Boolean Expression Practice
#Write a script that evaluates the five expressions below and prints each one with its result. Add a comment on each line explaining why the result is what it is:
#print(not True and False)
#print(True or False and False)
#print(not (5 > 3))
#print(10 == 10 and 4 != 4)
#print(not False or not True)
#Example format:
#False   # not True is False; False and False is False
#Save as: warmup3.py
#not True is False; and False is False
#print("not true, false")
#true or false is true; false and false is false
#print("True or false(false and false)")

#print(not True and False)
#print(True or False and False)
a=10
b=5
#1
print(not 10>5 and 10<5)
#a>b is 10>5 -->true ; a<b is 10<5 -->false :
#not true and false --> as per the Operator Precedence first priority for "not" :
#false and false --> false :

#2
print(20>10 or 20<10 and 20<10 )
#a>b is 10>5 --> ture or a<b is 10<5 --> false and a<b is 10<5--> false :
#True or False and False --> as per Operator Precedence we need to consider "and" equation then "or" :
#false and false -->false ; true or false --> true :

#3
print(not (30>20))
#not (10>5) --> true :
#not true --> false :

#4
print(40 == 40 and 50 != 50)
#a == a is 10 == 10 --> true ; and b != b is 5 != 5 -->false
#true and false --> false

#5
print(not 30>10 or not 30<10)
#a>b is 10>5 -->true ;  a<b is 10<5 -->false
#not true --> false ; not false --> true
#false or true --> true
