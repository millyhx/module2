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
userInput = int(userInput)
result = userInput - 2
print(result)

#CAN USE THE TYPE METHOD TO CHECK WHAT DATA
#TYPE THE INPUT IS. IF YOU ARE GIVING AN INTEGER
#AS THE INPUT FOR A STRING INPUT, IT WONT WORK.

userInput = input("Please give a number ")

def simpleOperation(userInput):
    intInput = int(userInput)
    result = intInput - 2
    return result

def nestedOperation():
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation()
print(result2)

#The first button in the debug panel is for you to start runing your code until the break point.
#The second button allows you to run your code line-by-line until the breakpoint
#The third one is for stepping into the sections (class and functions) that you would like to dig into more and the fourth button is for you to step out when you feel that the error is not related to the current section.
#The fifth button is for you to go to the next breakpoint, and the last square shaped button is for you to exit debugging mode and go back to normal coding mode.