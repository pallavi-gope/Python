#we are going to write a program that generates a random number and asks the user to guess it.
#if a user guess it higher than the actual number, the program displays "Lower number please".
#similarly if the user guess it too low, the program prints "Higher number please".
#when the user guesses correct number, the program displays the number of guesses, the player used to arrive at the number.
import random

randomNumber = random.randint(1, 100)
guesses = 0
userGuess = None

while userGuess != randomNumber:
    userGuess = int(input("Guess a number between 1 to 100 : "))
    if(userGuess == randomNumber):
        print("You guessed it right!")
    else:
        if(userGuess > randomNumber):
            print("You guessed it wrong! Lower Number Please")
        else:
            print("You guessed it wrong! Higher Number Please")

    guesses += 1       

print(f"Total Guesses : {guesses}")