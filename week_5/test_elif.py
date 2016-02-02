rawStr = raw_input('Entera number: ')
try:
	ival = int(rawStr)
except Exception, e:
	ival = raw_input('Plz Enter a real number: ')
if ival > 0:
	print "nice job"
else:
	print "Not a number"
	