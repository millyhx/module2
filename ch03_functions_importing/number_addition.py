# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:32:52 2018

@author: milly
"""
#VERSION 1
def user_add_number ():
    
    user_number1 = int(input("Enter a number: "))
    user_number2 = int(input("Enter a number: "))
    total_answer = user_number1 + user_number2
    print("")
    print("The total answer is {}".format(total_answer))

user_add_number()


#VERSION 2
def numbers_args(number1, number2):
    answer = number1 + number2
    print("{} plus {} is {}".format(number1,number2,answer))
    
numbers_args(5,10)
