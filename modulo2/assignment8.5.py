"""8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 
'From ' like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). Then print out a count at the end. 
Hint: make sure not to include the lines that start with 'From:'."""

fname = raw_input("Enter file name: ")
if fname == "":
	fname = "mbox-short.txt"
try:
	fh = open(fname)
except:
	print "Invalid file name!"
	fname = raw_input("Enter file name: ")
	exit()				#if I want to exit program just uncomment this line
	#continue			#if I want to ask again for the file name to the user >> not working at all
lst = list()
tmpLst = list()
count = 0
for line in fh:					#for to read the file
		line = line.rstrip()
		if not line.startswith('From '):
			continue
		count = count + 1	
		result = line.split()
		print result[1]
print "There were", count, "lines in the file with From as the first word"
	
	
