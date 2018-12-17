#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:15:17 2018

@author: milly
"""

#string formatting

age = 5 #here we are naming a variable age and giving it the value of 5.
like = "painting" #here we are naming a variable lik and giving it the value of the string painting.
age_description = "My age is {} and I like {}".format(age,like) #we have named a variable age_description which has a string value that calls the variables within. We can set which variables go where by using the format method that lays out the order in which the variables will be called.

print(age_description)#here we can print the variables to the console

