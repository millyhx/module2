# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:41:57 2018

@author: milly
"""

#--------------
#practice
#--------------

def user_details():
    user_name = input("What is your name? ")
    print("Hi, {}".format(user_name))
    user_choice = input("Would you like to buy a car? ")
    if user_choice == "no":
        print("No worries. See you soon. ")
    else:
        money()
        
def money():
    user_money = int(input("What is your maximum limit to spend? "))
    if user_money > 1000:
        print("You are willing to spend up to {}, is this correct? ".format(user_money))
        user_confirm = input()
        if user_confirm == "yes":
            buy_car()
        else:
            money()

    
def buy_car():
    print("k")
    
user_details()