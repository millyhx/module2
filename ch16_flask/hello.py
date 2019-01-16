# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:15:55 2019

@author: milly
"""

from flask import Flask
app = Flask("MyApp")

@app.route("/")

def homepage():
    return "<h1 style='color:blue'>Homepage</h1>"


@app.route("/about")

def about():
    return "<h1 style='color:green'>About Page</h1>"  


@app.route("/contact")

def contact():
    return "<h1 style='color:purple'>Contact Page</h1>"  
          
app.run(debug=True)

