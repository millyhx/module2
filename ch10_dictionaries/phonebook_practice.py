# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:13:59 2018

@author: milly
"""


def input_phone_book():
    phonebook = {}  
    users = 0
    while users < 4:
        print("-" * 50 )
#        queens_age = 92
        user1 = input("What's your name? ")
        phone_num = input("What is the last 3 digits of your phone number? ")
        lucky_num = input("What is your lucky number? If you don't know, take a guess. ")
        user_age = int(input("How old are you? "))
        town_city = input("What Town/City do you live in? ")
        
          
        users = users + 1
        if users == 4:
            print("Thank you for entering these details.")
            
            
        phonebook[user1] = (phone_num, lucky_num, user_age, town_city)    
        print (phonebook)
    print (phonebook)    
    return phonebook

  
phonebook = input_phone_book()

#CHALLENGE 1
##sort the dictionary by Name- alphabet
#phonebook = sorted(phonebook.items(), key=lambda kv: kv[0])
#
##sort the dictionary by Town/city - alphabet
#phonebook = sorted(phonebook.items(), key=lambda kv: kv[2])

#sort the dictionary by lucky number
#phonebook = sorted(phonebook.items(), key=lambda kv: kv[1])




