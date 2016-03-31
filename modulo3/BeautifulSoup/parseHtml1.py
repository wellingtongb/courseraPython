# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
from bs4 import BeautifulSoup
#url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/comments_42.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of anchor tags
#each tag is like a dictionary of HTML attributes
tags = soup.findAll('a')
for tag in tags:
    print tag.get("href", None)
