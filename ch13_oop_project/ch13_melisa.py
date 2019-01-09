# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:20:23 2019

@author: milly
"""
#################
#TASK 1
#################
#class Person:
#    def __init__(self,name,age,gender):
#        self.name = name
#        self.age = age
#        if gender == "m":
#            self.isMale = True
#        elif gender == "f":
#            self.isMale = False
#        else:
#            print("Gender not recognised!")
            
#################
#TASK 2
#################
         
class Person:
    def __init__(self,name,age,gender):
        def greetingInformal(self):
            print("Hi", self.name)
        def greetingFormal(self):
            if self.isMale:
                print("Welcome, Mr", self.name)
            else:
                print("Welcome, Ms", self.name)
                
#################
#TASK 3
#################

p1 = Person("Harry", 12, "m")
p2 = Person("Jean", 12, "f")
p1.greetingInformal()
p1.greetingFormal()
p2.greetingFormal()


#################
#TASK 4
#################

class Wizard(Person):
    def greetingFormal(self):
        print("Welcome, Mr", self.name, end='')
        print("-you\'re a fine wizard!")
        
