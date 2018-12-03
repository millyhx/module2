# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:56:43 2018

@author: milly
"""

#CONVERT LIBRARY

#convert temprature function


def convert_temprature(centigrade):
    fahrenheit = (centigrade * 9.0)/5.0 + 32
    kelvin = centigrade + 273.15
    print("Converting centigrade into fahrenheit and kelvin.")
    print("Centigrade in Fahrenheit:", fahrenheit)
    print("Centigrade in Kelvin:", kelvin)