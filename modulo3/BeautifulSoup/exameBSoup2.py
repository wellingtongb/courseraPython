# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/known_by_Freyja.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
count = 0
total = 18
newUrl = ""
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    count = count +1
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
                
                count = 0
                newUr2 = tag1.get('href', None)                 
                html2 = urllib.urlopen(newUr2).read()        
                soup2 = BeautifulSoup(html2)
                tags2 = soup2('a')
                for tag2 in tags2:
                    count = count +1
                    if (count == total):
                        print tag2.get('href', None)    #========   3
                        
                        count = 0
                        newUr3 = tag2.get('href', None)                         
                        html3 = urllib.urlopen(newUr3).read()                
                        soup3 = BeautifulSoup(html3)
                        tags3 = soup3('a')
                        for tag3 in tags3:
                            count = count +1
                            if (count == total):
                                print tag3.get('href', None)    #========4                                
                                
                                count = 0
                                newUr4 = tag3.get('href', None)                                 
                                html4 = urllib.urlopen(newUr4).read()                        
                                soup4 = BeautifulSoup(html4)
                                tags4 = soup4('a')
                                for tag4 in tags4:
                                    count = count +1
                                    if (count == total):
                                        print tag4.get('href', None)    #========5
                                        
                                        count = 0
                                        newUr5 = tag4.get('href', None)
                                         
                                        html5 = urllib.urlopen(newUr5).read()
                                
                                        soup5 = BeautifulSoup(html5)
                                        tags5 = soup5('a')
                                        for tag5 in tags5:
                                            count = count +1
                                            if (count == total):
                                                print tag5.get('href', None)    #========6
                                                
                                                count = 0
                                                newUr6 = tag5.get('href', None)
                                                 
                                                html6 = urllib.urlopen(newUr6).read()
                                        
                                                soup6 = BeautifulSoup(html6)
                                                tags6 = soup6('a')
                                                for tag6 in tags6:
                                                    count = count +1
                                                    if (count == total):
                                                        print tag6.get('href', None)    #========7
                                                        print tag6.contents[0]
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                