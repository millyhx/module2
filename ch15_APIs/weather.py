# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:33:51 2019

@author: milly
"""

import requests #importing the library requests

endpoint = "http://api.openweathermap.org/data/2.5/weather" 
payload = {"q":"London,UK", "units":"metric", "appid":"THIS IS WHERE YOU WOULD PUT THE API"}

response = requests.get(endpoint, params=payload)
data = response

print(response.url)
print(response.status_code)
print(response.headers["content-type"])
print(response.text)

