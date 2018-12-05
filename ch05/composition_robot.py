# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:28:20 2018

@author: milly
"""
class Animal():
    def eat(self):
        print("yum")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

class Robot():
    def move(self):
        print("... move move move...")

class CleanRobot(Robot):
    def clean(self):
        print("I vacuum dust")
        
        

class SuperRobot():
    
    def __init__(self):
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
        
    def move(self):
        return self.o1.move() 
    
    def bark(self):
        return self.o2.bark() 
    
    def clean(self):
        return self.o3.clean() 
    
    
    
machineDog = SuperRobot()
machineDog.move()
machineDog.bark()
machineDog.clean()