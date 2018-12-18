# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:58:43 2018

@author: milly
"""
#-------------------------
#ROCK PAPER SCISSOR GAME
#-------------------------
from random import randint
print("-----------------------")
print("  ROCK,PAPER,SCISSORS")
print("-----------------------")

def main_game():
    play_again = "yes"
    while play_again == "yes":
        player = input(" \n    ROCK     (r) \n    PAPER    (p) \n    SCISSORS (s)\n\n>>>  ")
        print(" ")
        print("     ",player, "VS", " ", end="")
        
        chosen = randint(1,3)
        
        #print(chosen)
        
        if chosen == 1:
            computer = "r"
        elif chosen == 2:
            computer = "p"
        else :
            computer = "s"
            
        print(computer)
        
        if player == computer:
            print("       DRAW!")
            play_again = input("    PLAY AGAIN? \n\n>>> ")
        elif player == "r" and computer == "s":
            print("<<< PLAYER WINS >>>")
            play_again = input("    PLAY AGAIN? \n\n>>> ")
        elif player == "r" and computer == "p":
            print("<<< COMPUTER WINS >>>!")
            play_again = input("    PLAY AGAIN? \n\n>>> ")
        elif player == "p" and computer == "r":
            print("<<< PLAYER WINS >>>")
            play_again = input("    PLAY AGAIN? \n\n>>> ")
        elif player == "p" and computer == "s":
            print("<<< COMPUTER WINS >>>")
            play_again = input("    PLAY AGAIN? \n\n>>> ")
        elif player == "s" and computer == "r":
            print("<<< COMPUTER WINS >>>")
            play_again = input("    PLAY AGAIN? \n\n>>> ")
        elif player == "s" and computer == "p":
            print("<<< PLAYER WINS >>>")  
            play_again = input("    PLAY AGAIN? \n\n>>> ")
        else:
            print("NOT A VALID INPUT. \n START AGAIN")
            main_game()
    
main_game()
#IMPORT RANDINT FROM RANDOM
#CREATE A PLAYER VARIABLE THAT STORES INPUT OF USER CHOICE
#CREATE A NEW VARIABLE THAT STORES A RANDOM INTEGER BETWEEN THE VALUES 1 AND 3
#IF THE RANDOM INT EQUALS 1 THEN THE COMPUTERS MOVE IS ROCK
#THE SAME APPLIES TO THE DIFFERENT INTS BUT WITH EITHER PAPER OR SCISSOR
#IF THE PLAYERS INPUT IS THE SAME AS THE COMPUTER THEN ITS A DRAW
#IF THE PLAYERS INPUT OVERTHROWS THE COMPUTERS OUTPUT THEN THEY WIN


