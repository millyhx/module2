# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:41:59 2018

@author: milly
"""
#using variables named in the parameters
def numbers_args(number1, number2):
    answer = number1 + number2
    print("{} plus {} is {}".format(number1,number2,answer))
    
numbers_args(5,10)


def hello_args(a,b,c,d):
    print("{} {} {} {}".format(a,b,c,d))
    
a = "hello"
b = "bye"
c = "love"
d = "coding"

hello_args(a,b,c,d)


#using previously stored variables

def names_args(a,b):
    print("You are called {} {}".format(a,b))

names_args("melisa", "huckle")