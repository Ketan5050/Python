import random
while(num): 
 num=random.randint(1,100)
if int(input("What is the square of {num}?"))==num**2:
    print("you are right")
else:
    print("you are wrong")
