# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:04:46 2018

@author: milly
"""

#Practice if statements



def enter_number():
    number = input("Enter a number between 1 and 10: ")
    number = int(number)
    
    if number >= 0 and number <=5:
        print ("Too low!") 
    elif number >= 6 and number <=10:
        print("Too high!")
    else:
        print("That's not a number between 1 and 10!")

enter_number()






