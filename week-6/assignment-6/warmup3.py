 #   Warmup 3: Scope in Action
#Demonstrate variable scope with two short examples in one file:

#Define a variable inside a function. Try to access it outside the function and show the NameError — paste the error in a comment, then remove or comment out the line that causes it.
#Show how return solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.


#def total_score():
#    score = 50

#total_score()
#print(score)  # NameError: name 'score' is not defined


#After fix

def total_score():
    score =95
    return score # send the results to outer call
    

my_score = total_score() # assigned return value to global variable
print(my_score) 


