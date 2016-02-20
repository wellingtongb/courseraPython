"""9.4 Write a program to read through the mbox-short.txt and figure out
who has the sent the greatest number of mail messages. The program looks for
'From ' lines and takes the second word of those lines as the person who sent the mail. 
he program creates a Python dictionary that maps the sender's mail address to a count of
the number of times they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
myList = list()
myDict = dict()
biggest = None
sender = ""

name = raw_input("Enter file")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for lines in handle:            #running through the file
    lines = lines.rstrip()      #cutting the blank spaces
    words = lines.split()       #spliting every word in a separete word
    if len(words) < 1:continue  #guardian to avoid blank lines and them avoid trace back
    if words[0] != "From":continue  #checking if lines starts with from, case not just go next
    myList.append(words[1])     #inserting the second value [1] inside myList
    
for occur in myList:            #for to run through my dictionary
    myDict[occur] = myDict.get(occur,0) + 1 #searching for occurrencies and adding into key, and also incrementind values
    for key,values in myDict.items():       #two iterator to run in each Tuple together
        if values != None and values > biggest: #searching for biggest value
            biggest = values                #Adding the biggest value found into the variable
            sender = key                    #adding the key from biggest value into variable
#print myDict

print sender, biggest


