# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:58:43 2018

@author: milly
"""

from random import randint

player = input("rock (r), paper (p), scissors (s)? ")

print(player, "vs")

chosen = randint(1,3)
print(chosen)

if chosen == 1:
    computer = "r"
elif chosen == 2:
    computer = "p"
else :
    computer = "s"
    
print(computer)

if player == computer:
    print("DRAW!")
elif player == "r" and computer == "s":
    print("Player wins")
elif player == "r" and computer == "p":
    print("Computer wins!")
elif player == "p" and computer == "r":
    print("Player wins")
elif player == "p" and computer == "s":
    print("Computer wins!")


