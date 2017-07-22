#DIY Number Guesser, by Josh Curfman
#Generates a random number and has the user guess it.

from random import randint

guessed=1

while guessed>0:
    print("I\'m going to pick a number between 1 and 256.")
    num=randint(1,256)
    while guessed==1:
        x=int(input("Please guess a number: "))
        if x<1:
            print("That\'s too low, please pick a new number.")
            guessed=2
        elif x>256:
            print("That\'s too high, please pick a new number.")
            guessed=2
        else:
            if x>num:
                print("Too high.")
            elif x==num:
                print("You got it!")
                guessed=2
            elif x<num:
                print("Too low.")
    if guessed==2:
        y=raw_input("Would you like to play again? Yes=y, No=N\n")
        no="N"
        yes="y"
        if y==yes:
            guessed=1
        elif y==no:
            guessed=0