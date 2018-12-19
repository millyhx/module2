# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:09:05 2018

@author: milly
"""

def convert_currency():
    user_pounds = float(input("What amount (£) would you like to convert? "))
    euro = user_pounds + 0.12
    dollar = user_pounds + 0.27
    japanese_yen = user_pounds + 143.66
    rupees = user_pounds + 88.68
    
    
    print("Pounds into euros:€", euro)
    print("Pounds into dollars:$", dollar)
    print("Pounds into Japanese Yen:¥", japanese_yen)
    print("Pounds into Indian Rupee:₹", rupees)
    
convert_currency()