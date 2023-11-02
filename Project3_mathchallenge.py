"""here we are going to generate random math problems for the user to complete.
   it will return the amount of time user take to solve those problems."""

#first going to import a random module .
import random
#Importing time module .
import time
OPERATORS=["+","-","*"]
MAX_VALUE=12
MIN_VALUE=3
TOTAL_PROBLEMS=10
#now going to make a function that will generate random math problems.
def generate_problems():   
    left=random.randint(MIN_VALUE,MAX_VALUE)
    right=random.randint(MIN_VALUE,MAX_VALUE) 
    #The choice() pickany value present in the variable.
    operator=random.choice(OPERATORS)
    expr=str(left)+" "+operator+" "+str(right)
    #As we also want the computer to know the answer we are -7
    #going to use the eval() function.
  #it will evaluate the python expression and give us answer.
    answer=eval(expr)
    #print(expr,answer)
    return expr,answer
wrong=0
print(input("Press enter to start"))
print("------------------------")
#As soon as user will press enter the timer will start.give result in seconds.
start_time=time.time()
for i in range(TOTAL_PROBLEMS):
    expr,answer=generate_problems()
    while True:
        guess=input("Problem #"+str(i+1)+": "+expr+"=")
        if guess==str(answer):
            break
        wrong+=1
end_time=time.time()
total_time=round(end_time - start_time,2 )       
print("-------------------------")        
print("Nice Work! you have completed it in",total_time,"sec")

