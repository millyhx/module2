# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:50:39 2018

@author: milly
"""

#metal = {}
#keys = iron, gold, zinc, lead
#values = tuple or list
#values = density, share prices, experiments
#sort the dictionary by the 0 position, reverse order


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








