# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:01:22 2018

@author: milly
"""

import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

def password_creator():
 number = input('How many passwords? ')
 number = int(number)

 length = input('How long would you like it to be? ')
 length = int(length)

 print('\nHere are your passwords:')

 for pwd in range(number):
   password = ''
   for c in range(length):
     password += random.choice(chars)
   print(password)

#main function
def user_name():
    name = input('What is your name? ')
    print('')
    print('Hello, {}!'.format(name).title())
    user_choice = input('Would you like me to create you a secure password? ').lower()
    
    if user_choice == 'yes':
        return password_creator()
    else: 
        print('')
        print('Okay, Goodbye')
    
user_name()


