
"""read the file, search for all digits using Regular expression, and them return the sum
of these numbers"""
import re

x= open("actualText.txt",'r').read()
y = re.findall('[0-9]+', x)
print sum(int(i) for i in y)
#print sum(int(i) for i in y) #invoke function sum then declare a int i and run through the lissty