# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:00:24 2018

@author: milly
"""

class Animal():
    def eat(self):
        print("yum")

class Dog(Animal):
    def bark(self):
        print("Woof")

class Cat(Animal):
    def meow(self):
        print("Meow")


Snoopy = Dog()
Snoopy.bark()
Snoopy.eat()

Monty = Cat()
Monty.meow()
Monty.eat()