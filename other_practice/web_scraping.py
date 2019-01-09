# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:30:07 2019

@author: milly
"""

import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

#soup.find_all("p")--- this will print out all of the p tags within the webpage.
#soup.find_all('p')[0].get_text()--- this will print out just the text within the p tag.

#soup.find_all(id="first")--- search for elements by ID


