# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:13:36 2018

@author: milly
"""

#lambda and dictionaries

#create a dictionary


#
#counts = {"a": 3, "c": 1, "b": 5}
#labels = list(counts.keys())
#labels.sort(key=lambda v:counts[v])
#
#sorted(labels, key=lambda v:counts[v])
#sorted(counts.items(), key=lambda kv: kv[1])


abc = {1:("greg", "january", 7), 2:("anna", "october", 3), 3:("mag", "november", 13)}

abc_keys = list(abc.keys())
abc_keys.sort(key=lambda k:abc[k][2])

