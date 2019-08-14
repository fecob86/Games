#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import libraries
import numpy as np
import math


# In[ ]:


# Welcoming user
name = input("What is your name? \n")
print("Hi, ",name,". Welcome to the Guess The Number game!")


# In[ ]:


def main():
# Choosing range limits and set target
    wrongMin = True

    while wrongMin == True:
        minRangeInput = input("Choose the lower limit for the range you want to play with.\n")
        try:
            minRange = int(minRangeInput)
        except ValueError:
            print("Wrong input. Please choose an integer number.\n")
        else:
            minRange = int(minRangeInput)
            wrongMin = False

    wrongMax = True

    while wrongMax == True:
        maxRangeInput = input("Choose the upper limit for the range you want to play with.\n")
        try:
            maxRange = int(maxRangeInput)
        except ValueError:
            print("Wrong input. Please choose an integer number.")
        else:
            maxRange = int(maxRangeInput)
            if maxRange <= minRange:
                print("Wrong input. Please choose a number greater than ",minRange,".")
            else:
                wrongMax = False

    setRange = [minRange,maxRange]
    print("Great! Your chosen range is ",setRange," (Range limits inclusive)")

    target = np.random.randint(minRange,maxRange + 1)

    # Picking and Assessing the Guess

    maxGuesses = 5
    guesses = []

    for ii in range(maxGuesses):
        wrongGuess = True

        while wrongGuess == True:
            guessInput = input("Choose your guess. Pick a number between {} and {} (Range limits inclusive)\n".format(minRange,maxRange))
            try:
                guess = int(guessInput)
            except ValueError:
                print("Wrong input. Pick a number between ",minRange," and ",maxRange)
            else:
                guess = int(guessInput)
                if guess < minRange or guess > maxRange:
                    print("Your guess is outside the chosen range. Pick a number between ",minRange," and ",maxRange)
                else:
                    wrongGuess = False
        
        guesses.append(guess)
        if guesses[ii] > target:
            print("Your guess was too high.\n")
        elif guesses[ii] < target:
            print("Your guess was too low.\n")
        else:
            print("Nailed it! Your guess is correct.\n")
            break

    print("Your guesses were: ",guesses,)
          
    if target in guesses:
          print("It took you ",len(guesses)," attepts to win the game.\n")
    else:
          print("Sorry, but you didn't guess.\n")
    return


# In[ ]:


main()


# In[ ]:


# Ask if wants to play again?
playAgain = False

while playAgain == False:
    ask=input("Do you want to play again? (Y/N) \n")
    if ask != "Y" and ask != "y" and ask != "N" and ask != "n":
        print("Sorry, didn't get that. Please respond Y or N.\n")
    elif ask == "Y" or ask == "y":
        main()
    else:
        print("Thank you for playing, ",name)
        break

exit()


# In[ ]:




