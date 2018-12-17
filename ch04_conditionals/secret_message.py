# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:20:30 2018

@author: milly
"""
#variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
import datetime

def user_input():
    name = input("What is your name? ")
    print("")
    print("Hello, {}!".format(name).title())
    user_choice = input("Would you like me to encrypt some text for you? (yes/no) ").lower()
    
    if user_choice == "yes":
        return encrypt_message()
    else: 
        print("")
        print("Okay, bye")
    

#Asks the user to input a key and a message
def encrypt_message():
    key = int(input("Enter a key: "))
    newMessage = " "
    message = input("Please enter a message: ")

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (position + key) % 26
            newCharacter = alphabet[newPosition]
            newMessage += newCharacter
        else:
            newMessage += character
    
    
    print("Your new message is: ", newMessage)
    user_time_choice()
    
def user_time_choice():
    user_decision = input("Would you like to know the time? (yes/no)  ")
    print("")
    
    if user_decision == "yes":
        return date_and_time()
    else: 
        print('')
        print('Okay, bye')
    
  
def date_and_time():
        
    print("The current time is: " ,                                          datetime.datetime.now().time())
    
user_input()