# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:09:56 2018

@author: milly
"""

#---------------
#DICE ROLL GAME
#---------------
from random import randint
min_dice = 1
max_dice = 6

roll_again = "yes"


while roll_again == "yes" or roll_again == "y":
    print("-----------------")
    print(" THE VALUES ARE:")
    print("-----------------")
    print("DICE 1", '| ', end='')
    print("DICE 2")
    print('  ', randint(min_dice, max_dice), ' ', end='')
    print('    ', randint(min_dice, max_dice))
    print("-----------------")
    roll_again = input("  ROLL AGAIN? \n\n>>> ")
    
#IMPORT THE RANDINT FUNCTION FROM RANDOM
#CREATE TWO VARIABLES, THE MIN AND MAX DICE VALUES
#CREATE A ROLL AGAIN VARIABLE WITH THE VALUE YES
#WHILE ROLL AGAIN EQUALS YES...
#PRINT RANDOM INTEGERS TWICE, WITIN THE BOUNDARIES OF THE
#MIN AND MAXIMUM VALUES.
#ASSIGN ROLL AGAIN A NEW VALUE OF INPUT
    
    