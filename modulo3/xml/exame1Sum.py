#Assignment for week 5 - parsing XML

import urllib
import xml.etree.ElementTree as ET


url = "http://python-data.dr-chuck.net/comments_235148.xml "

xml = urllib.urlopen(url).read()
tree = ET.fromstring(xml)

counts = tree.findall('.//count')

total = 0

for count in counts:
    total = total + int(count.text)
print total