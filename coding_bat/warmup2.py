# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:12:53 2018

@author: milly
"""

#CODING BAT WARMUP 2

#string_times
def string_times(str, n):
  return str * n

#front_times
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result

#string_bits
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

#string_splosion
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

#last2
def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[len(str)-2:]
  count = 0
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1
  
  return count

#array_count9
def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count = count + 1
  
  return count