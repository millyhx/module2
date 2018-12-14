# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:55:53 2018

@author: milly
"""

#syntax for dictionary 
#{key1:value1, key2:value2}


#empty dictionary
salary = {}
phonebook = {}

#assigning a valueto a new key:
salary["al"] = 20000
salary["bo"] = 50000
salary["co"] = 70000

phonebook["milly"] = 863 #07554990863
phonebook["mari"] = 885
phonebook["seraphine"] = 385 

#update the value of a key:
salary["al"] += 2000

phonebook["milly"] = 3863
phonebook["mari"] = 8885
phonebook["seraphine"] = 3385

#delete a value of a key:
del phonebook["milly"]

#get keys and values from a dictionary
phonebook.keys()
phonebook.values()

#storing a variable with the keys value
phonebook_keys = list(phonebook.keys())

x = "milly"
if x in phonebook:
    print(x, ":", phonebook[x])
else:
    print(x, "not found!")

