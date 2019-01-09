# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:24:31 2019

@author: milly
"""

import sqlite3

conn = sqlite3.connect("phonebookDatabase.db")
c = conn.cursor()

def create_table_business():
    c.execute('CREATE TABLE IF NOT EXISTS BTBusinessPhoneBook(businessName TEXT, addressLine1 TEXT, addressLine2 TEXT, postcode TEXT, telephoneNum REAL, businessCategory TEXT, xCor REAL, yCor REAL)')
    
def data_entry():
    c.excute('INSERT INTO BTphoneBook VALUES(Country Cars and Vans, CCV Limited, Station Road, TA41AY, 01823279081, Motor Vehicle,51.041031,-3.311750)')
    
    conn.commit()
    c.close()
    conn.close()
    
def create_table_people():
    c.execute('')