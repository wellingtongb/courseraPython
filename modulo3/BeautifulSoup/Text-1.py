# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
#url = "http://python-data.dr-chuck.net/comments_42.html"
url = "http://python-data.dr-chuck.net/comments_235151.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
soma = 0
for tag in tags:
   # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('span', None)
    #print 'Contents:',tag.contents[0]
    #print 'Attrs:',tag.attrs
    soma = soma + int(tag.contents[0])

print soma
    