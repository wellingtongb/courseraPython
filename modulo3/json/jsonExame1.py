import json
import urllib

url = "http://python-data.dr-chuck.net/comments_235152.json"
source = urllib.urlopen(url).read()     #using urlib to retrieve all data from website

info = json.loads(source)       #creating a json object or dictionaire from our data
total = 0
for item in info['comments']:
    #print "NAME ===== ", item['name']
    #print "COUNT ===== ", item['count']
    total = total + int(item['count'])

print total

