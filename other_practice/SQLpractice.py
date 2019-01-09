# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:59:42 2019

@author: milly
"""

import sqlite3

conn = sqlite3.connect("millyDatabase.db")
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS millyRawData(firstName TEXT, lastName TEXT, age REAL)')
    
def data_entry():
    c.execute('INSERT INTO millyRawData VALUES("Melisa", "Huckle", 19)')
    c.execute('INSERT INTO millyRawData Values("Jade", "Griffiths", 19)')

    conn.commit()
    c.close()
    conn.close()
    
    
create_table()
data_entry()
