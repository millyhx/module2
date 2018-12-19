# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:45:34 2018

@author: milly
"""

#----------------
#CREATING A LIST
#----------------

my_fav_fruits = ["apple", "orange", "banana"]

x = ["this", 55, "that", my_fav_fruits]

#----------------
#MODIFY THE LIST
#----------------

#delete an item in the list
x.remove(my_fav_fruits)

#update the list item value by using the index of the item
x[1] = "and"

#update the list
x.append("again")

#----------------
#SLICING A LIST
#----------------

#include items in position 1-3, not 4
x[1:4]

#----------------
#SORTING A LIST
#----------------

#y will return a copy of the list (x) but 
#in order of ascending numerical values.
x = [7,11,3,9,2]
y = sorted(x)

#----------------
#TUPLES
#----------------

a = [0,1,2,3,4,5,6,7,8,9]
del a[-1]

b = (0,1,2,3,4,5,6,7,8,9)
del b[-1]

a = [0,1,2,3,4,5,6,7,8,9]
a[0] = 50

b = (0,1,2,3,4,5,6,7,8,9)
b[0] = 50

a.append("z")
print(a)

b = (0,1,2,3,4,5,6,7,8,9)
b.append("z")

#----------------
#USING LAMBDA
#----------------

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["aa", "sb", "lf", "hw", "ed", "fy"]
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)

x2 = [("a", 3, z), ("c", 1, y), ("b", 5, x)]
sorted(x2, key=lambda s:s[1])

#------------------
#LOOPING WITH LISTS
#------------------
my_favourite_fruits = ["apple", "orange", "banana"]
for x in my_favourite_fruits:
    print(x)
    
#--------------------------
#IF STATEMENTS WITHIN LISTS
#--------------------------
my_favourite_fruits = ["apple", "orange", "banana"]
if "apple" in my_favourite_fruits:
    print("Yes, apple is in the list")

#---------------------------------------
#SHOWING HOW MANY ELEMENTS ARE IN A LIST
#---------------------------------------
my_favourite_fruits = ["apple", "orange", "banana"]
print(len(my_favourite_fruits))

#---------------------------------------
#DELETING SPECIFIED ELEMENTS
#---------------------------------------
my_favourite_fruits = ["apple", "orange", "banana"]
del my_favourite_fruits[0]
print(my_favourite_fruits)


