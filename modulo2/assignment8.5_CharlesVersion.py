
""" This program was freaking out because it can't handle with empty lines
so we create a guardiam for it"""

fhand = open("mbox-short.txt")

for line in fhand:
	line = line.rstrip()
	words = line.split()
	#if words == [] :continue	#this is first version of a guardioan to prevent crash
	if len(words) < 1:continue 	#this another version
	if words[0] != "From":continue
	print words[2]	
