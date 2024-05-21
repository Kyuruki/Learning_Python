import random

#number the user guesses later in the game
user_guess = 0
guess_amount = 0

#Generates number between 0,100 and assigns it to R
r = random.randrange(0,101)

#asks user if it wants to play a guessing game
play = input("Do you want to play a game? ")

if play.lower() == "yes":
    print("Okay lets go! ")
else:
    quit()

#while the user guess isn't correct, run a for loop for 
while int(user_guess) != r:
    user_guess = input("Guess the number: ")
    if int(user_guess) > r:
        print("Whoops too high: ")
        guess_amount += 1
    elif int(user_guess) < r:
        print("whoops too low: ")
        guess_amount += 1
    elif int(user_guess) == r:
        print("YOU GOT IT: ")
        guess_amount += 1
    
#Once user inputs correct answer, display printed statement
print("The answer was " + str(r) + ".")
print ("It took you " + str(guess_amount) + " tries to guess the answer")

        





