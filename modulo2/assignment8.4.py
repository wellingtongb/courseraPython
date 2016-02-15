"""8.4 Open the file romeo.txt and read it line by line. For each line, split the line into 
a list of words using the split() function. The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not 
append it to the list. When the program completes, sort and print the resulting words in 
alphabetical order. """

fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print "Invalid file name!"
	fname = raw_input("Enter file name: ")
	exit()				#if I want to exit program just uncomment this line
	#continue			#if I want to ask again for the file name to the user >> not working at all
lst = list()
tmpLst = list()
for line in fh:					#for to read the file
	tmpLst = line.split()		#adding lines at tmpList
	for words in tmpLst:		#reding each word at each line in tmplist
		if words not in lst:	#verifying if the word is on lst (attention  here lst is clear)
			lst.append(words)	#if in lst there isn't the word, add the word for lst
lst.sort()
print lst
