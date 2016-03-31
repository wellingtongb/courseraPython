# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
count = 0
total = 18
iteracao = 0
newUrl = ""
# Retrieve all of the anchor tags
tags = soup('a')
i = 0


for tag in tags:
    count = count + 1
    if (count == total):
        print tag.get('href', None)     #=========  1
        count = 0
        newUrl = tag.get('href', None)              
        html1 = urllib.urlopen(newUrl).read()
        
        soup1 = BeautifulSoup(html1)
        tags1 = soup1('a')
        for tag1 in tags1:
            count = count +1
            if (count == total):
                print tag1.get('href', None)    #========== 2
    
 
    
                

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                