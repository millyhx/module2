# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:59:38 2019

@author: milly
"""

def alphabet(word):
    result = ""
    for i in range(1, len(word) + 1):
        if i % 3 == 0:
            result += word[i-1].upper()
        else:
            result += word[i-1]
    return result


word = "abcdefghijklmnopqrstvuwxyz"
print(alphabet(word))   
    
#Write the letters 'A' to 'Z' (in upper case) to the console, placing each letter on a new line.
#
    
    
#For every third letter, write it to the console in lowercase instead.
#
    
    
#For every fourth letter, write its numeric position in the alphabet to the console instead (e.g. instead of outputting 'D' output '4').
#
    

#If a letter satisfies both rules 2 and 3, write out its numeric position followed by the letter in lowercase (e.g. 'L' should be output as '12l').