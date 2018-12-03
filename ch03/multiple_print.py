# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:29:41 2018

@author: milly
"""

def how_many_times ():
    user_name = input("What is your name? ")
    print("Hello {}".format(user_name))
    multiple_print = int(input("How many times shall I print your name? "))
    total_prints = user_name * multiple_print
    print(total_prints)
    
how_many_times()