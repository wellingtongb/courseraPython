"""7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average 
of those values and produce an output as shown below. 
 when you are testing below enter mbox-short.txt as the file name."""

fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print "Invalid file name!"
	fname = raw_input("Enter file name: ")
	exit()				#if I want to exit program just uncomment this line
	#continue			#if I want to ask again for the file name to the user >> not working at all
cont = 0
total = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue #if there isnt this string in the line go next
    cont = cont + 1
    #print "cont", cont
    line = line.rstrip()				#removing the white spaces and new lines from file
    pos = line.find(':')				#searching for : in each line and save the position
    textSliced = line[pos+1:]			#slicing the line to keep only numbers
    value = float(textSliced)			#converting strings to float number
    total = total + value
    average = total/cont
print "Average spam confidence:",average