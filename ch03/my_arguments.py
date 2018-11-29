# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:14:11 2018

@author: milly
"""

def add_two_numbers_from_args(number1,number2):#here we are defining a function with two arguments.
    answer = number1 + number2 #the variable answer equals the two arguments.
    print("{} plus {} is {}".format(number1,number2, answer)) #here we print what the function was for using a format method.
    
add_two_numbers_from_args(50,10) #we call the function here whilst stating the two arguments.


def your_name_from_args(first_name,last_name):
    print("Your first name is {} and your last name is {}".format(first_name,last_name))

your_name_from_args("milly","huckle")






