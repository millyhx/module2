# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:55:07 2019

@author: milly
"""

import sqlite3
import requests

 
conn = sqlite3.connect('phonebook_project.db')
c = conn.cursor()

  
endpoint = 'https://api.postcodes.io/postcodes/'
postcode = 'TA41AY'
response = requests.get(endpoint + postcode)
data = response.json()
print (response.url)          
print(data)
latitude = data['result']['latitude']
longitude = data['result']['longitude']
print(latitude)
print(longitude)
