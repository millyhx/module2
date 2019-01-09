# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:08:34 2019

@author: milly
"""
###########################
#IMPORTING MODULES
###########################

import sqlite3
import time
import datetime
import random

#########################
#CONNCTING THE DATABASE
#########################

conn = sqlite3.connect("task1.db")
c = conn.cursor()
    
#IMPORT THE SQLite TOOLKIT
#IMPORT ALL OF THE OTHER MODULES AND FUNCTIONS
#CONNECT THE DATABASE AND CREATE THE DATABASE
#CONNECT THE CURSOR (LOW LEVEL POINTER TO FIND POSITIONS OF DATA IN EACH TABLE)


###########################
#CREATING THE DATABASE
###########################

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

#CREATE A TABLE USING THE EXECUTE FUNCTION
#CREATE TABLE IF NOT EXISTS IS THE COMMAND TO CHECK THE TABLE EXISTS.
#STUFF TO BUILD IS THE DATABASE TABLE NAME
#UNIX, DATESTAMP, KEYWORD AND VALUE ARE THE COLUMN NAMES IN DATABASE.

###########################
#INSERTING DATA INTO TABLES
###########################
    
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()

#INSERT INTO ALLOWS US TO PUT DATA INTO THE TABLE
#WE PREVIOUSLY CREATED COLUMNS, SO NOW WE NEED TO INSERT 4 VALUES INTO THE TABLE.
#AFTER INSERTING, YOU NEED TO RUN THE COMMAND. 
#ONCE THE PROCESS IS COMPLETE, YOU NEED TO CLOSE THE TABLE AND DATABASE.
    
################################
#INSERTING DATA USING VARIABLES
################################

#INSERT DATA DYNAMICALLY
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    
    c.execute("INSERT INTO stuffToBuild(unix,datestamp,keyword.value) VALUES (?,?,?,?)", (unix,date,keyword,value))
    
    conn.commit()

#INSERT MULTIPLE ROWS WITH A FOR LOOP
    for i in range(10):
        dynamic_data_entry()
        time.sleep(1)#SLOWS DOWN THE PROCESS
        
    c.close()
    conn.close()
    
############################
#READING DATA FROM DATABASES
############################

#THE SELECT STATEMENT
def read_from_db_all():
    c.execute("SELECT * FROM stuffToBuild WHERE value=8")
    for row in c.fetchall():
        print(row)

#THE SELECT COMMAND IN SQL IS USD TO ONLY READ THE DATA COLUMNS BASED ON OUR CHOICE. 
#AFTER CHOOSING, THERE IS A FROM COMMAND THAT POINTS TO WHICH DATA TABLE WE ARE SELECTING FROM.
#A WHERE CLAUSE IS USED FOR FURTHER FILTERING THE DATA INSIDE EACH COLUMN.
#FETCHALL() = SIMILAR TO THE PULL FUNCTION IN GIT.
    
#####################
#DATA SELECT EXERCISE
#####################

def read_from_db2():
    c.execute("SELECT * FROM stuffToBuild WHERE value =8 and unix > 1534855733 and unix <1534855741 ")
    for row in c.fetchall():
        print(row[0])
        

    