# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:08:52 2018

@author: milly
"""

class Robot():
    def move(self):
        print("...move move move...")

class CleanRobot(Robot):
    def clean(self):
        print("I vacuum dust")

class CookRobot(Robot):
    def cook(self):
        print("I make rice")
        
MillyRobot = CleanRobot()
MillyRobot.move()
MillyRobot.clean()

JadeRobot = CookRobot()
JadeRobot.move()
JadeRobot.cook()