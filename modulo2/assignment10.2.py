"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution
by hour of the day for each of the messages. You can pull the hour out from the
'From ' line by finding the time and then splitting the string a second
time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour,
print out the counts, sorted by hour as shown below.
Desired out put
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
myList = list()
myDict = dict()

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:             #go through my file
    line = line.rstrip()        #striping blank spaces
    words = line.split()        #splitting in separated words
    if len(words) < 1:continue  #guardin to avoid crash with blank lines
    if words[0] != "From":continue  #checking if our line starts with "from "
    hour = words[5]             #adding our full hour in one variable
    hour  = hour.split(':')     #splitting by ":"
    finalhour = hour[0]         #taking only the first value
    myDict[finalhour] = myDict.get(finalhour, 0) + 1    #adding to my dictionary 
    
for k, v in myDict.items():
    myList.append( (k, v) )
myList.sort()

for k, v in myList:
    print k, v




  
        

