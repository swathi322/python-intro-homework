#Write your own eligibility or decision script. It can check anything — event admission, a discount, a quiz result, a recommendation — as long as it meets these requirements:

#Collects input from the user with at least two input() calls
#Uses at least one if/elif/else chain with at least three branches
#Uses at least one boolean operator (and, or, or not)
#Prints a different, meaningful message for at least three different combinations of input
#Share your work in the Slack #[class]-discussion channe

#My code will calculate Investment based on mentioned income and expenses
#mentioned income and expenses
#income = 100,200,300
#expense= 100,150,200
#Invest = 0  , 50,100

income=int(input("Enter a income: "))
expense=int(input("Enter a expenses: "))
if income==100 and expense==100:
 print(f"My income is ${income} and my expenses is ${expense}, My investment is $0")
elif income >=200 and expense <=150:
 print(f"My income is ${income} and my expenses is ${expense}, my investment is $50 ")
elif income >=300 and expense <=200:
 print(f"my income is ${income} and my expenses is ${expense}, my investment is $100")
else:
 print ("Enter mentioned income and expenses")