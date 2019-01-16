# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:10:05 2019

@author: milly
"""
###########################
#IMPORTING MODULES
###########################

import requests

###########################
#TASK 1
###########################

def send_simple_message():
    return requests.post(
        "----MAILGUN DOMAIN----",
        auth=("api", "----USER API----"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox395ddfcbf9be4b08a469b5e723fdceaa.mailgun.org>",
              "to": "Melisa Huckle <millycyb@outlook.com>",
              "subject": "Hello Melisa Huckle",
              "text": "Congratulations Melisa Huckle, you just sent an email with Mailgun!  You are truly awesome!"})

###########################
#TASK 2
###########################
    
endpoint = "http://api.openweathermap.org/data/2.5/weather" 
payload = {"q":"London,UK", "units":"metric", "appid":"THIS IS WHERE YOU WOULD PUT THE API"}

response = requests.get(endpoint, params=payload)
data = response.json()

print(response.url)
print(response.status_code)
print(response.status_code)
print(response.headers["content-type"])
print(response.text)

###########################
#TASK 4
###########################

temprature = data['temp']
name = data['name']
weather = data['weather'][0]['main']
print (u'its {} C in {}, and the sky is {}'.format(temprature,name,weather))


###########################
#CALL THE FUNCTIONS
###########################
    
send_simple_message()

