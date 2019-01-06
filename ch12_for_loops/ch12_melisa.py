# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:33:14 2018

@author: milly
"""

#------------------
#THE FOR LOOP
#------------------

#------------------
#TASK 1
#------------------

#LOOP THROUGH A LIST USING A FOR LOOP
my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]

for item in my_shopping_cart:
    print (item)
    
#------------------
#TASK 2
#------------------
    
#UPDATE LIST VALUES
values = [875, 23, 451]

for val in values:
    print("---> "+ str(val))
    
#------------------
#TASK 3
#------------------
    
#CREATE YOUR OWN LIST
values = ["this", 55, "that"]
for item in values:
    print("***", item)
    
#------------------
#TASK 4
#------------------

#LOOP THROUGH A STRING TYPE
for char in "Yes":
    print(char)

#------------------
#TASK 5
#------------------

#LOOP THROUGH A TUPLE
x = (1,2,3,4,5)

for y in x:
    print (y)
    
#------------------
#TASK 6
#------------------

#CREATE A SALARY DICTIONARY

salary_dictionary = {"al":20000, "bo":50000, "ced":1500}

salary = list(salary_dictionary.keys())

salary.sort(reverse=True, key=lambda k:salary_dictionary[k])

for x in salary:
    print(x)

#METAL DICTIONARY
densities = {"iron":(7.8, 50, 3), "gold":(19.3, 70, 9), "zinc":(7.13, 90, 15), "lead":(11.4, 20, 1)}

metals = list(densities.keys())

metals.sort(reverse=True, key=lambda m:densities[m])

keyValue = sorted(densities.items(), key=lambda kv:kv[1][1], reverse=True)

#KEY AND THE VALUE RETRIEVAL
for metal, metalValue in keyValue:
    print(metal, metalValue[1])

for metal in metals:
    print(metal, densities[metal])

for metal in metals:
    print(metal, densities[metal][1])
    
#for metal in metals:
#    print("{0:>8} = {1:5.1f}".format(metals,densities[metals]))
    
#------------------
#TASK 8
#------------------
for metal in metals:
    if densities[metal][0]>8:
        print(metal,densities[metal][0])
    
#for the items in metal,if the dictionary items 
#in the first index positions are greater than 8, 
#print out the key and then the value in position 9.  
    
#------------------
#TASK 9
#------------------

#DESIGN A SUM FUNCTION
values = [3, 12, 9]
total = 0

for val in values:
    total += val
print("TOTAL:" + str(total))

#here we have created a list 
#created a variable with the value 0
#In the for look we have said for values
#in valus... total += val, so total is equal to the sum
#(total = total + val)
#of the values. Then we print the total sum. 

#REMEMBER TO CAST DATA TYPES INTO ONE TYPE
#WHEN NOT USING FORMAT PRINTING.

def sumValues(l):
    sumV = 0
    for val in l:
        sumV +=val
        return sumV
print (sumValues(values))

#------------------
#TASK 10
#------------------

#USING A LOOP WITH INDEX VALUES
range(3)
for i in range(len(values)):
    values[i] = values[i] * 2

#arguments give start, end, and step values.
#so the range would start from 3 and go up by 
#two each time but no exceed 10 which is the end value.

for i in range(3,10,2):
    print(i)
    
#------------------
#FOR LOOP EXERCISE
#------------------

wish_list = {"socks":5, "chocolate":10, "clothes":3}

gifts = list(wish_list.keys())

for gift, item in wish_list.items():
    if item >= 3:
        print("I got ", item, "of ", gift, ".")
    else:
        print("oh no")

#------------------
#TASK 12
#------------------

nums = [2,3,65,23,123,432,3]
for n in nums:
    if n > 100:
        print("found", n)
        break


nums = [1,5,30,200,101,100,22]

for index in range(len(nums)):
    print("loop index", index, "with value", nums[index])
    
    if nums[index] > 100:
        print("break :" , nums[index], "with index", index)
        break

#NESTED LOOPS
outer_vals = [1,2,3]
inner_vals = ["A", "B", "C"]
for oval in outer_vals:
    for ival in inner_vals:
        print(oval, ival)

#we have two lists- outer vals and inner vals
#for the items in the outer vals list
#find the items in the inner vals list 
#print those items. 


#MULTIPLICATION TABLE
for i in range(1,7):
    for j in range(1,11):
        print("{0:>3}".format(i * j), end='')
    print('\n')
    

colours = ["red", "green", "red", "green", "blue", "green", "green"]
d = {}
for item in colours:
    if item not in d:
        d[item] = 1
        print(d, "first time")
    else:
        d[item] = d[item] + 1
        print(d)

