#Your program will generate a random integer in the range 1 to 10
#The user will receive three guesses to determine the integer.
#After each guess your program will inform the user whether the guess was correct, too high, or too low.
#If the user does not guess the number correct within 3 tries, the program will print the correct answer.

import random

x = random.randrange(1,11)
# print(x)  # this was here so I could test each of the conditional statements while knowing the answer

for a in range(2): #the first two guesses can be in one loop because the answers to each guess are the same
    guess = int(input("What number am I thinking of?"))
    if guess > x:
        print("That is too high, try again.")
    elif guess < x:
        print("That is too low, try again")
    else:
        print("That's right!")
        exit()

finalguess = int(input("This is your last guess:"))

if finalguess > x: #the third guess needs to be examined outside of the previous loop because it also needs to give the correct answere
    print("That's to high, the answer is: " + str(x))
elif finalguess < x:
    print("That's too low, the answer is: " + str(x))
else:
    print("Finally! Thats's right!")
