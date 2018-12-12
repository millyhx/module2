# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:56:33 2018

@author: milly
"""
#
def DataBundlePurchase(truePasscode, balance):
    count = 0
    while count < 3:
        passcode = input("ENTER PIN: ")
        if passcode == truePasscode:
            print("---LOGIN SUCCESSFUL---")
            return user_input(balance)
        else:
            print("---LOGIN FAILED")
            count += 1


def checkBalance(balance):
   if balance > 0:
       return True
   else:
       return False
   
def credit_report(balance):
    print ("\nYour balance is £{}".format(balance))
   
def purchase_data(balance):
    return buy_data(balance)
   
def user_input(balance):
    user_choice = input(" Would you like to: \n\n Request credit balance (1) \n Purchase data bundle (2) \n Exit the program (3) \n\n>>> ")
    
    if user_choice == "1":
        return credit_report(balance)
    elif user_choice == "2":
        return purchase_data(balance)
    elif user_choice == "3":
        print("Exiting program...")
    else:
        return user_input(balance)


def multipleOfFive(amount):
    return amount == int(amount / 5.0) * 5

def buy_data(balance):
    maxTopUp = 100.00
    print("Enter your mobile phone number:")
    number1 = input()
    print("Please RE-enter the number of the phone: ")
    number2 = input()
    
    if number1 == number2:
        print("𝗠𝗮𝘅 𝘁𝗼𝗽-𝘂𝗽 𝗮𝗺𝗼𝘂𝗻𝘁 𝗶𝘀 £𝟭𝟬𝟬")
        print("|||Top-up amount must be a multiple of 5 pounds|||")
        amount = float(input("Please enter your top-up amount: \n>>>"))
        
        if amount > maxTopUp:
            print("Amount exceeds maximum permitted top-up")
            print("Request refused")
            return "top-up-request:refused"
        
        elif amount > balance:
            print("Amount exceeds available funds")
            print("Request refused")
            return ("top-up-request", amount)
        
        elif multipleOfFive(amount):
            print ("Transaction authorised")
            print("Your new accounts balance is", round(balance - amount), "GBP")
            user_input(balance)
            return ("top-up-request", amount)
        
        else:
            print("Amount is not a multiple of 5")
            print("Request refused")
            return "top-up-request:refused"
    else:
        print("Error: the two numbers entered are different.")
        print("Transaction cancelled")
        return "top-up-request:refused"
            
