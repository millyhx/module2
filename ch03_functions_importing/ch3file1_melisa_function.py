# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:28:39 2018

@author: milly
"""

#-------------------------
#INPUT FROM A USER
#-------------------------

#print("What is your name? ")
#name = input()
#print("Hello {}!".format(name))

#-------------------------
#INTRODUCING FUNCTIONS
#-------------------------

#print("What's your name? ")
#name = input()
#print("Hello {}!".format(name))


def add(a,b):
    return print(a + b)

#ADDING TWO NUMBERS FROM ARGUMENTS

def add_two_numbers_from_args(number1, number2):
    answer = number1 + number2
    print("{} plus {} is {}".format(number1, number2, answer))


#----------------------------
#USING RANGE WITHIN ARGUMENTS
#----------------------------

#print (range(10))
#print (range(1,10))
#print (range(1,10,2))


#----------------------------
#FUNCTION PRACTICE
#----------------------------

#Converting Distances:
def convert_distance(miles):
    kilometers = (miles * 8.0)/5.0
    convert_distance = "{} miles to km is {}".format(miles,kilometers)
    print(convert_distance)
    return convert_distance


#Converting Temprature:
def convert_temp(centigrade):
    fahrenheit = centigrade * 9.0 / 5.0 + 32
    kelvin = centigrade + 273.15
    temprature_convert = "The temprature from centigrade to fahrenheit is {}, and {} in kelvin".format(fahrenheit, kelvin)
    print(temprature_convert)
    return temprature_convert



