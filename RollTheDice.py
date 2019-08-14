#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Libraries import
import math
import numpy as np


# In[ ]:


# Welcome User
name = input("What is your name? \n")
print("Hi, ",name,". Welcome to the Roll the Dice game!")


# In[ ]:


# Definition of PlayGame function
def playgame():
    wrongAnswer=True
    minRolls=1
    maxRolls=5

    while wrongAnswer == True:
        q_Roll=input("How many times do you want to roll the dice? You can roll the dice up to {} times.\n".format(maxRolls))
        try:
            q_Roll=int(q_Roll)
        except ValueError:
            print("Wrong input. Please choose a number between {} and {} (both inclusive).\n".format(minRolls,maxRolls))
        else:
            q_Roll=int(q_Roll)
            if (q_Roll > maxRolls) or (q_Roll < minRolls):
                print("Wrong input. Please choose a number between 1 and 5 (both inclusive).\n")    
            else:
                print("Great! You chose to roll the dice ",q_Roll," times.\n")
                wrongAnswer = False

    results=[0]*q_Roll
    total=0

    for ii in range(q_Roll):
        results[ii]=np.random.randint(q_Roll)+1
        total+=results[ii]

    print("Your results are ",results," and Your total score is ",total)
    return


# In[ ]:


# Call PlayGame function
playgame()


# In[ ]:


# Ask if wants to play again?
playAgain = False

while playAgain == False:
    ask=input("Do you want to play again? (Y/N) \n")
    if ask != "Y" and ask != "y" and ask != "N" and ask != "n":
        print("Sorry, didn't get that. Please respond Y or N.\n")
    elif ask == "Y" or ask == "y":
        playgame()
    else:
        print("Thank you for playing, ",name)
        break

exit()


# In[ ]:




