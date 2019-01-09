# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:08:34 2019

@author: milly
"""

import sqlite3
conn = sqlite3.connect("task1.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
    
#CREATE TABLE IF NOT EXISTS--- is the command we use to create and check table existence. 
#stuffToBuild is the database table name
#unix, datestamp, keyword and value are the column names in the database.

###########################
#INSERTING DATA INTO TABLES
###########################
    
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()
    