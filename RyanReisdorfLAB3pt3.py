import random
x=(random.randint(1,10))
guess=int(input("Enter number guess: "))
if guess==x:
	print("Correct")
else:
	print("Incorrect")
