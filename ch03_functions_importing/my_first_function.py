# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:59:44 2018

@author: milly
"""

def hello_world():

    #def get_user_name():
        user_name = input("What is your name? ").title()
        print("Hello {}".format(user_name))
        
def add_two_numbers():
        number1 = 1
        number2 = 2
        answer = number1 + number2
        print ("{} plus {} is {}".format(number1, number2, answer))
        

hello_world()
add_two_numbers()
     



