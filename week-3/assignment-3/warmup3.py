 
#a=10
#b=5
#1
#print(not 10>5 and 10<5)
print(not True and False)
#10<5 evaluate to false.
#Operator Precedence first priority for "not":
#not true becomes false.

#2
#print(10>5 or 10<5 and 10<5)
print(True or False and False)
#10>5 evaluate to ture.
#10<5 evaluate to false.
#Operator Precedence and evaluates to false.
#remaining statement True or False, 
#which is true.

#3
#print(not (10>5))
print(not (True))
#10>5 evaluate to true.
#Operator Precedence shows not,
#which means not true.
#not true become false.

#4
#print(10 == 10 and 5 != 5)
print(True and False)
#10 == 10 evaluate to true.
#5 != 5 evaluate to false.
#Operator Precedence and evaluate to false
#which is false.

#5
#print(not 10>5 or not 10<5)
print(not True or not False)
#10>5 evaluate to true. 
#10<5 evaluate to false.
#Operator Precedence first priority for "not",
#not true becomes false.
#not false becomes true.
#not false or not true.
#which is true.

