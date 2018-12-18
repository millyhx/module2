# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:41:59 2018

@author: milly
"""
#------------
#VERSION 1
#------------

def hello_args(a,b,c,d):
    print("{} {} {} {}".format(a,b,c,d))
    
a = "hello"
b = "bye"
c = "love"
d = "coding"

hello_args(a,b,c,d)

#------------
#VERSION 2
#------------

def names_args(a,b):
    print("You are called {} {}".format(a,b))

names_args("melisa", "huckle")

#------------
#VERSION 3
#------------

def add_two_numbers_from_args(number1,number2):#here we are defining a function with two arguments.
    answer = number1 + number2 #the variable answer equals the two arguments.
    print("{} plus {} is {}".format(number1,number2, answer)) #here we print what the function was for using a format method.
    
add_two_numbers_from_args(50,10) #we call the function here whilst stating the two arguments.


#VERSION 3

def your_name_from_args(first_name,last_name):
    print("Your first name is {} and your last name is {}".format(first_name,last_name))

your_name_from_args("milly","huckle")
