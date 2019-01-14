# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:10:05 2019

@author: milly
"""
#--------------First of all we need to import requests
import requests


#--------------Create a function so that we can put the information about sending
#--------------an email into.
def send_simple_message():
    return requests.post(
        "----MAILGUN DOMAIN----",
        auth=("api", "----USER API----"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox395ddfcbf9be4b08a469b5e723fdceaa.mailgun.org>",
              "to": "Melisa Huckle <millycyb@outlook.com>",
              "subject": "Hello Melisa Huckle",
              "text": "Congratulations Melisa Huckle, you just sent an email with Mailgun!  You are truly awesome!"})
# You can see a record of this email in your logs: https://app.mailgun.com/app/logs

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10,000 emails/month for free.

    
#--------------Then call the function so that it runs.
send_simple_message()

