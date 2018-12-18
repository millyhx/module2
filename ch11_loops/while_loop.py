# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:22:13 2018

@author: milly
"""
#------------
#WHILE LOOPS
#------------

#TASK 1
#Code Purpose: Prints a series of values by repeatedly dividing the initial value by 2.

x = 33
while x >= 1:
    print(x, ": ", end='')
    x = x/2
print(x)

#SET THE VARIABLE X TO HAVE A VALUE OF 33
#WHILE X IS BIGGER OR EQUALS TO 1
#PRINT X, A SEMI COLON AND END
#THE 'END' METHOD ENDS THE OUTPUT WITH A SPACE
#WE THEN DIVIDE THE X BY 2
#PRINT THE VARIABLE X

#------------------------------------------------------

#TASK 2
#Code Purpose: To compute triangular numbers when given an input n.

def triangle(n):
    number = 0
    while n > 0:
        number = number + n
        n = n -1
    return number


#DEFINE A FUNCTION CALLED TRAINGLE
#GIVE IT AN ARGUMENT OF 'N'
#WHILE N IS MORE THAN 0
#NUMBER = NUMBER PLUS THE ARGUMENT
#ARGUMENT EQUALS ARGUMENT - 1
#RETURN THE NUMBER

#------------------------------------------------------

#TASK 3
#Code Purpose: To create a loop that determines if student marks are pass/fail/first

#question_pass = "yes"
#
#while question_pass == "yes":
#    mark = int(input("Enter user mark: "))
#    mark = int(mark)
#    print("Mark is", mark, end='')
#    if mark >= 70:
#        print(" - first class!")
#    elif mark >= 40:
#        print("- that's a pass")
#    else:
#        print("- that's a fail")
    

#SET THE VARIABLE MARK TO 1
#WHILE MARK IS MORE THAN 0
#MARK = USER INPUT IN AN INTEGER FORMAT
#PRINT A STATEMENT THAT ALLOWS USER TO KNOW WHAT THE CURRENT MARK IS
#IF STATEMENT TO SHOW DIFFERENT OUTPUTS DEPENDING ON MARK INPUT

#------------------------------------------------------

#TASK 4
#Code Purpose: Early exit and continuation
    
i = 55
while i > 10:
    print (i)
    i = i * 0.8
    if i == 35.2:
        break

#CREATE A VARIABLE I WITH VALUE 55
#WHILE I IS GREATER THAN 10
#PRINT I
#I EQUALS I TIMES 0.8
#IF I EQUALS 35.2 THEN STOP THE PROGRAMME (BREAK)

#------------------------------------------------------
#TASK 5

#Code Purpose: Prints a greeting for the name entered until the user enters done.

def greeting():
    
    
    while True:
        name = input("Enter name: ")
        if name == "exit":
            break
        print("Hello, ", name)

#WHILE THE STATEMENT IS TRUE
#NAME = INPUT (ASK FOR THE NAME)
#IF THE NAME IS EQUAL TO DONE
#STOP THE PROGRAM
#OTHERWISE, PRINT HELLO AND THE NAME GIVEN FROM INPUT
