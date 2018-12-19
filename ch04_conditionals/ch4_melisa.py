# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:04:46 2018

@author: milly
"""

#------------------
#CONDITIONALS
#------------------

def enter_number():
    number = input("Enter a number between 1 and 10: ")
    number = int(number)
    
    if number >= 0 and number <=5:
        print ("Too low!") 
    elif number >= 6 and number <=10:
        print("Too high!")
    else:
        print("That's not a number between 1 and 10!")

enter_number()

age = input("Enter your age")
age = int(age)

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
elif age < 65:
    print("Adult")
else:
    print("Pensioner")
    
#------------------
#PSEUDOCODE
#------------------
#IN ORDER TO SOLVE A PROGRAMMING PROBLEM, YOU NEED STEP BY STEP INSTRUCTIONS WHICH
#CAN OTHERWISE BE RECOGNISED AS AN ALGORITHM. TO PLAN AN ALGORITHM WE CAN IMPLEMENT
#IT IN DIFFERENT LANGUAGES OR EVEN STATE IT IN PLAIN ENGLISH.

#EXAMPLE:
#MAKE A CUP OF (INSTANT) COFFEE:
#1.FILL KETTLE
#2.BOIL KETTLE
#3.PUT SPOON OF COFFEE IN CUP.
#4.FILL CUP (NEARLY) WITH WATER FROM KETTLE.
#5.ADD DASH OF MILK