# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:14:13 2018

@author: milly
"""

def convert_distance(miles):
    kilometers = (miles * 8.0)/5.0
    print("Converting distance in miles to kilometers.")
    print("Distance in miles:", miles)
    print("Distance in kilometers:", kilometers)
    
convert_distance(44)

print("")
print("")

def convert_temprature(centigrade):
    fahrenheit = (centigrade * 9.0)/5.0 + 32
    kelvin = centigrade + 273.15
    print("Converting centigrade into fahrenheit and kelvin.")
    print("Centigrade in Fahrenheit:", fahrenheit)
    print("Centigrade in Kelvin:", kelvin)
    
convert_temprature(44)

print("")
print("")

def convert_currency(pounds):
    euro = pounds + 0.12
    dollar = pounds + 0.27
    japanese_yen = pounds + 143.66
    rupees = pounds + 88.68
    
    print("Converting pounds into different currencies.")
    print("Pounds into euros:€", euro)
    print("Pounds into dollars:$", dollar)
    print("Pounds into Japanese Yen:¥", japanese_yen)
    print("Pounds into Indian Rupee:₹", rupees)
    
convert_currency(20)