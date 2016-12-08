import random
x = random.randint(1,100)

guess = 0
tries = 0

guess = int(input("I am thinking of a random number between 1 and 100. Guess what it is?"))
tries = tries+1

while guess  != x :
    while guess < x:
        guess = int(input("No, my number is higher than "+str(guess)+ ". Please try again: "))
        tries = tries+1
    while guess > x:
        guess = int(input("No, my number is lower than "+str(guess)+ ". Please try again: "))
        tries = tries+1

while guess == x:
    print("Well done! Your answer was "+str(guess)+ " and you found it in "+str(tries)+ " guesses.")
    print("the program will now end.")
    quit()

