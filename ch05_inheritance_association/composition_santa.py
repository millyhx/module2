# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:57:43 2018

@author: milly
"""

class present():
    def user_present(self):
        print("You will recieve a present!")

class bad_present(present):
    def user_bad_present(self):
        print("You will not recieve a present!")


class Santa():
    def __init__(self):
        self.o1 = bad_present()
        self.o1 = present()
    
    def user_present(self):
        return self.o1.user_present
    def user_bad_(self):
        return self.o2.user_bad_present
    


HoHoHo = Santa()
HoHoHo.user_present()
HoHoHo.user_bad_present()