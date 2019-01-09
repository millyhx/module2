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
    