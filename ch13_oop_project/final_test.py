# -*- coding: utf-8 -*-
"""
Created on Sun Jan 06 17:36:10 2019

@author: Milly
"""

from MovingShapes import *
frame = Frame(500, 500)

# All the shapes
amount = 2
shapes = []

for i in range(amount):
    shapes.append(Square(frame, 80))
    shapes.append(Diamond(frame, 80))
    shapes.append(Circle(frame, 80))

while True:
    for shape in shapes:
        shape.moveTick()



 