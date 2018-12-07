# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:49:03 2018

@author: milly
"""

#Inheritance Practice

class FavouriteFood():
    def __init__(self, name, age=0):
        self.name = name
        
    def eat(self):
         print('yum')
         
class Food(FavouriteFood):
    def __init__(self, name, age=0,foodNumber=0):
        self.foodNumber = foodNumber
        
    def foodBank(self):
        print("You love {}\n".format(name)*self.foodNumber)
        
        
class foodAgent(Food):
    def detect(self):
        if self.foodNumber>=3:
            print("Stop eating...")
        
        
name = input("What is your favourite food? ")        
age = int(input("How many times have you eaten it today? "))
bark = int(input("How many times have you eaten it this week? "))

import sys
name = sys.argv[1:]
age = sys.argv[age]

userFood = foodAgent(name, age, bark)
userFood.foodBank()
userFood.eat()
userFood.detect()