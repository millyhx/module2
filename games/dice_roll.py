# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:09:56 2018

@author: milly
"""

#Dice rolling simulator
import random
min_dice = 1
max_dice = 6

roll_again = "yes"


while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are...")
    print(random.randint(min, max))
    print(random.randint(min, max))
    
    roll_again = input("Roll the dices again? ")