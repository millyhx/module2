#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:15:17 2018

@author: milly
"""
#------------------
#STRING INPUT
#------------------

#NAMING A VARIABLE AND ASSIGN THE VARIABLE OF INPUT
name = input("What is your name? ")
print("Hello!, Your name is " + name.upper())

age = input("How old are you, " + name + "? ")
print(" You are " + age)

fav_color = input("What is your favourite colour? ")
print(" Your favourite colour is " + fav_color)

print("")

print("This is what I know about you.. " + "Your name is " + name + ", you are " + age + " and" " your favourite colour is " + fav_color + ".")


#------------------
#SPLITTING A STRING
#------------------

#CREATE A VARIABLE

strExample = "a.b.c.d.e" 

#SPLIT THE STRING WHERE THE FULL STOPS ARE

SplitStr = strExample.split(".")

#PRINT IT TO THE CONSOLE

print(SplitStr)


