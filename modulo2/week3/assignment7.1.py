"""7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output """
#use words.txt as the file name
fname = raw_input("Enter file name: ")
newFh = fname + ".txt"		#adding a suffix to the user file name
print newFh
try:
	fh = open(newFh)	
except:
	print "Invalid file name!!"	
	exit()
for line in fh:
	line = line.rstrip()
	print line.upper()