# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:09:07 2018

@author: milly
"""
""" A customer of ABC Bank with a checking account. Customers have the following properties: Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
        
Return a Customer object whose name is *name* and starting balance is *balance*.
Return the balance remaining after withdrawing *amount* dollars. Return the balance remaining after depositing *amount* dollars. """

#-----------
#TASK 1
#-----------

class Customer(object):

    def __init__(self,name,balance=0.0):

        self.name = name
        self.balance = balance

    def withdraw(self,amount):

        if amount > self.balance:
            raise RuntimeError("Amount greater than available balance.")
            self.balance -= amount
            return self.balance

    def deposit(self,amount):

        self.balance += amount
        return self.balance

jason = Customer("Jason Taylor", 1000.0)


#---------------
#TASK 2,3 AND 4
#---------------

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