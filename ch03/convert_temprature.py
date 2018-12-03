# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:11:53 2018

@author: milly
"""
#VERSION ONE

celsius = float(input("What's the temperature in your city today? "))

def tempConverter(celsius):

   fahrenheit = celsius * 9.0 /5.0 + 32
   kelvin = celsius + 273.15

   print("That's" ,  fahrenheit ,  "degrees in Fahrenheit and" , kelvin , "degrees in Kelvin.") 

tempConverter(celsius)



#VERSION TWO

def convert_temp ():
    centigrade = int(input("What temprature in Celsius do you want to convert? "))
    print("")
    fahrenheit = centigrade*9.0/5.0 + 32
    kelvin = centigrade + 273.15   
    print("Converting temp in Celsius to Farenheit and Kelvin...")
    print("The temprature in Fahrenheit is {}, and the temprature in Kelvin is {}".format(fahrenheit,kelvin))
    
    return(kelvin,fahrenheit)

convert_temp()


#VERSION THREE
print("Returning the temprature from a variable stored within...")
def convert_temprature(centigrade):
    fahrenheit = (centigrade * 9.0)/5.0 + 32
    kelvin = centigrade + 273.15
    print("Converting centigrade into fahrenheit and kelvin.")
    print("Centigrade in Fahrenheit:", fahrenheit)
    print("Centigrade in Kelvin:", kelvin)
    
convert_temprature(44)