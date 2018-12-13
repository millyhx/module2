# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:50:41 2018

@author: milly
"""

import random

print ('=' * 11)
print("HANGMAN")
print ('=' * 11, '\n')
    
def get_guess():
    
    dashes = "-" * len(secret_word)
    guesses_left = 15
    
    
    while guesses_left > 1 and not dashes == secret_word:
        
        print(dashes)
        print (str(guesses_left))
        
        guess = input("Guess a letter: >>>  ")
        
        if len(guess) != 1:
            print("Your guess must only be one character!")
        elif guess in secret_word:
            print("✔")
            dashes = update_dashes(secret_word, dashes, guess)
        else:
            print("✘")
            guesses_left -= 1
            
    if guesses_left < 0:
        print("UNLUCKY! The word was : " + str(secret_word))
    else:
        print("WELL DONE! You win. The word was: " + str(secret_word))
        
def update_dashes(secret, cur_dash, rec_guess):
    result = ""
    
    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result = result + rec_guess
        else:
            result = result + cur_dash[i]
            
    return result

words = ["bagpipes", "awkward", "banjo", "oxygen"]

secret_word = random.choice(words)
get_guess()