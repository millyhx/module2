# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:49:14 2018

@author: milly
"""

import random
import datetime
import time

def luckyNumberRandom():
    name = input("Please type your name here: ")
    print("Hello " + name.upper())
    number = int(input("Please enter a number: "))
    
    print("Your lucky number is: " + str(random.randint(50,number)))
    
startTime = time.time()

print("date and time", datetime.datetime.now())
print()
print("current time" , datetime.datetime.now().time())

processTime = time.time()-startTime

print()
print("Program running time: ", round(processTime,2), "second")

luckyNumberRandom()