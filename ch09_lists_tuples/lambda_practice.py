# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:45:28 2018

@author: milly
"""

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
myFavF = ["apple", "orange", "banana"]
x = ["aa", "sb", "lf", "hw", "ed", "fy"]
z = ["fg", "uj", "sx", "uj", "ww", "cf"]
y = sorted(x)

x2 = [("a", 3, z), ("c", 1, y), ("b", 5, x)]
sorted(x2, key=lambda s:s[1])

