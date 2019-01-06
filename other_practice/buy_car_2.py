# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 19:12:06 2018

@author: milly
"""

def user_details():
    print("What is your first name? ")
    first_name = input()
    print("What is your last name? ")
    last_name = input()
    print("Do you want to buy a car? ")
    user_choice = input()
    
    if user_choice == "yes":
        print("You have chosen to buy a car")
    else:
        ("You have not entered correct details")
        