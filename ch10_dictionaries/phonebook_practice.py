# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:13:59 2018

@author: milly
"""


def input_phone_book(phonebook):
    print("-" * 50 )
    user1 = input("What's your name? ")
    phone_num = input("What is the last 3 digits of your phone number? ")
    lucky_num = input("What is your lucky number? If you don't know, take a guess. ")
    user_age = int(input("How old are you? "))
    town_city = input("What Town/City do you live in? ")
    
    phonebook[user1] = (phone_num, lucky_num, user_age, town_city)
    
    
    age_difference = 92 - user_age
    
    user_choice = input("Add another user? ")
    if user_choice == "yes":
        phonebook = input_phone_book(phonebook)
        return phonebook
    else:
        print(user1, ": You are ", age_difference, "years younger than the queen.")
        return phonebook

phonebook = {}    
phonebook = input_phone_book(phonebook)

#CHALLENGE 1
##sort the dictionary by Name- alphabet
#phonebook = sorted(phonebook.items(), key=lambda kv: kv[0])
#
##sort the dictionary by Town/city - alphabet
#phonebook = sorted(phonebook.items(), key=lambda kv: kv[2])

#sort the dictionary by lucky number
phonebook = sorted(phonebook.items(), key=lambda kv: kv[1])




