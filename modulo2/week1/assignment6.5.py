
"""6.5 Write code using find() and string slicing (see section 6.10) to extract the number 
at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
#version 1
text = "X-DSPAM-Confidence:    0.8475";
loc = text.find('0')
print float(text[loc:])"""

#version 2
text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
print pos
textSliced = text[pos+1:]
print textSliced
newT = textSliced.replace(' ','')	#using replace to remove space from string
print newT

#Charles severance version 
text = "X-DSPAM-Confidence:    0.8475";
print x 	#only to check if python is working well
pos = x.find(':')
num = float(x[pos+1:])
print num, type(num)