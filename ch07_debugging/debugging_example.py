# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:57:42 2018

@author: milly
"""

userInput = input("please give a number: ")
result = userInput - 2

#WHEN I RUN THIS CODE, THIS ERROR SHOWS:
#TypeError: unsupported operand type(s) for -: 'str' and 'int'

userInput = input("please give a number: ")
print(type(userInput))

#CAN USE THE TYPE METHOD TO CHECK WHAT DATA
#TYPE THE INPUT IS. IF YOU ARE GIVING AN INTEGER
#AS THE INPUT FOR A STRING INPUT, IT WONT WORK.