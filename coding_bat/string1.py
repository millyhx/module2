# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:07:40 2018

@author: milly
"""

#CODING BAT STRING 1

#hello_name
def hello_name(name):
  return "Hello " + name + "!"

#make_abba
def make_abba(a, b):
  return a + b + b + a

#make_tags
def make_tags(tag, word):
  return ("<" + tag + ">" + word + "</" + tag + ">")

#make_out_word
def make_out_word(out, word):
   return out[:2] + word + out[2:]

#extra_end
def extra_end(str):
  str = str[-2:]
  return str * 3

#first_two
def first_two(str):
    return(str[:2])
    
#first_half
def first_half(str):
  return str[:len(str) // 2]

#without_end
def without_end(str):
  return str[1:-1]

#combo_string
def combo_string(a, b):
  return a+b+a if len(a)<len(b) else b+a+b

#non_start
def non_start(a, b):
  return a[1:]+b[1:]

#left2
def left2(str):
  return str[2:]+str[:2]

