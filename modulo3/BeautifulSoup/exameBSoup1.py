# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/comments_235151.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('href')
soma = 0
for tag in tags:
    soma = soma + int(tag.contents[0])

print soma
    