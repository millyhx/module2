# -*- coding: utf-8 -*-
"""
Created on Sun Jan 06 17:36:10 2019

@author: Milly
"""

from Shapes import *
from pylab import random as r


class MovingShape:
    def __init__(self, frame, shape, diameter):

        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)

        #Here I am initialising X and Y, they are also made                             half of the diameter. 
        self.x = self.diameter / 2
        self.y = self.diameter / 2

        # Here I am making the shapes move randomly
        self.dx = 10 
        self.dy = 10 
        
        #if the random integer chosen is less than 0.5 then 10 - 1.
        if (r() < 0.5):
            self.dx = self.dx * -1 
        else:
            self.dy = self.dy * -1
        
        #This is where the shapes will start moving from. The start position. 
        self.minx = self.diameter / 2
        self.maxx = frame.width - self.minx

        self.miny = self.diameter / 2
        self.maxy = frame.height - self.miny

        # Moving the X and Y values. 
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)
        
        self.goto(self.x, self.y)
        
    def goto(self, x, y):
        self.figure.goto(x, y)
    
    def moveTick(self):
        self.x += self.dx
        self.y += self.dy
        if (self.x < self.minx):
            self.x = self.minx + self.dx
            self.dx = abs(self.dx)   
        elif (self.x >= 0) and (self.x > self.maxx):
            self.x = self.maxx - self.dx
            self.dx = self.dx * -1
        if (self.y < self.miny):
            self.y = self.miny + self.dy
            self.dy = abs(self.dy)   
        elif (self.y >= 0) and (self.y > self.maxy):
            self.y = self.maxy - self.dy
            self.dy = self.dy * -1
          
        self.figure.goto(self.x, self.y)
        
        
####################
#THE THREE SHAPES
####################
        
class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'square', diameter)
        
class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'diamond', diameter)
        
        self.minx = self.diameter * 0.7
        self.maxx = frame.width - self.minx

        self.miny = self.diameter * 0.7
        self.maxy = frame.height - self.miny

        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)

        
class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, 'circle', diameter)
