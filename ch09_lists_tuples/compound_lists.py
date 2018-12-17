# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:15:34 2018

@author: milly
"""
#looping within lists
my_favourite_fruits = ["apple", "orange", "banana"]
for x in my_favourite_fruits:
    print(x)

#if statements within lists
my_favourite_fruits = ["apple", "orange", "banana"]
if "apple" in my_favourite_fruits:
    print("Yes, apple is in the list")

#showing how many elements are in a list
my_favourite_fruits = ["apple", "orange", "banana"]
print(len(my_favourite_fruits))

#deleting specified elements
my_favourite_fruits = ["apple", "orange", "banana"]
del my_favourite_fruits[0]
print(my_favourite_fruits)


x = ["the", "cat", "sat"]
y = ["on", "the", "mat"]
z = x + y
print(z)

x = ["this", "and", "that", "once", "again"]
x[1:2]
print(x)

x = [7,11,3,9,2]
sorted(x)
[2,3,7,9,11]
sorted(x,reverse =True)
[11,9,7,3,2]
print(x)
