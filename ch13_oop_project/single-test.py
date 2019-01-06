# -*- coding: utf-8 -*-
"""
Created on Sun Jan 06 17:36:10 2019

@author: Milly
"""

from functionsMove import *

frame = Frame(300,300)
square = Square(frame, 60)
circle = Circle(frame, 75)
diamond = Diamond(frame, 73)

for i in range(100):
    square.moveTick()
    circle.moveTick()
    diam.moveTick()
