# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:55:53 2018

@author: milly
"""

#syntax for dictionary 
#{key1:value1, key2:value2}

#---------------------
#CREATING A DICTIONARY
#---------------------

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

#---------------------
#AVOIDING KEY ERRORS
#---------------------
tel = {"alf":111, "bobby":222, "calvin":333}

k = "eric"
if k in tel:
    print(k, ":", tel[k])
else:
    print(k, "not found")
    
#you can check if a key is present in a dictionary
#with a test in the form of a KEY in DICT, which
#returns True or False.

#---------------------
#SORTING A DICTIONARY
#---------------------
    
metal = {}

metal["iron"] = (7.8, 50, 3)
metal["gold"] = (19.3, 70, 9)
metal["zinc"] = (7.13, 90, 15)
metal["lead"] = (11.4, 20, 1)


metal_info = list(metal.keys())

#using sort method
#metal_info.sort(reverse=True,key=lambda k:metal[k][1])

#using sorted by value
sorted(metal.items(), key=lambda kv: kv[0]) #return key and value
sorted(metal, key=lambda k: metal[k]) #return only key

#sort by key
sorted(metal.items(), key=lambda kv: kv[0])
sorted(metal)

#sort by (2nd position of the) values:
sorted(metal.items(), key=lambda kv: kv[1][2])
sorted(metal, key=lambda k: metal[k][2])
