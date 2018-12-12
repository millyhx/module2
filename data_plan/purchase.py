# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:38:17 2018

@author: milly
"""

def DataPurchase(truepin,balance):
    if checkPIN(truepin):
        print("\nPlease choose your transaction type:")
        print(" -to request balance -enter 1")
        print(" -to top-up a data bundle -enter 2")
        
        transactionType = input("\nEnter your choice: ")
        
        if (transactionType == "1"):
            print("Your balance is", balance, "GBP")
            print ("Thank you for using this service.")
            return "balance-request"
        
        elif transactionType == "2":
            return mobileTopUp(balance)
        else:
            print("Error: transaction type not recognised.")
            return "transaction-error"
    else:
        print("\nError: PIN authorisation failed - exiting.")
        return "PIN-error"
    
    
def checkPIN_once(truepin):
    attempt = input("Please enter your PIN: ")
    if attempt == truepin:
        return True
    else:
        print ("PIN incorrect")
        return False

def checkPIN(truepin):
    if checkPIN_once(truepin):
        return True
    print("\nPlease try again (2nd attempt).")
    if checkPIN_once(truepin):
        return True
    print ("\nPlease try again (final attempt).")
    if checkPIN_once(truepin):
        return True
    return False

def multipleOfFive(amount):
    return amount == int(amount / 5.0) * 5

def mobileTopUp(balance):
    maxTopUp = 100.00
    print("Please enter the number of the mobile phone you wish to top-up: ")
    number1 = input()
    print("Please RE-enter the number of the phone: ")
    number