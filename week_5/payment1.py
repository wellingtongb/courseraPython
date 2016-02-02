hours = raw_input('Enter the hours amount: ')
try:
	iHours = float(hours)
except Exception, e:
	print 'You need to insert a numeric value.'

rate =  raw_input('Enter a rate value: ')
try:
	iRate = float(rate)
except Exception, e:
	print 'You need to insert a numeric value to Payment rate.'

if iHours > 45:
	payment = iHours * iRate * 1.5
	print "Your payment will be: " + str(payment)
else:
	payment = iHours * iRate
	print "Less them 40 hours. So your payment will be: " +str(payment)
