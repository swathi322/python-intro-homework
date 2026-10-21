
#My code will calculate Investment based on mentioned income and expenses
#mentioned income and expenses
#income = 100,200,300
#expense= 100,150,200
#Invest = 0  , 50,100

income=int(input("Enter income: "))
expense=int(input("Enter expenses: "))
if income==100 and expense==100:
 print(f"My income is ${income} and my expenses are ${expense}, My investment is $0 :)")
elif income ==200 and expense ==150:
 print(f"My income is ${income} and my expenses are ${expense}, my investment is $50 :)")
elif income ==300 and expense ==200:
 print(f"my income is ${income} and my expenses are ${expense}, my investment is $100 :)")
else:
 print ("Enter mentioned income and expenses")