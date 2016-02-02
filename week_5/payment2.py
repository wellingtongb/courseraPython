hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = 10.5
extraHour = h - 40
rateExtra = rate * 1.5
#print rateExtra
totalExtra = rateExtra * extraHour
#print totalExtra

if h > 40:
	#its necessary to pay the first 40 hours normal rate and them only the extra hour pay more 1.5
	h = h - extraHour
	payment = (h * rate) + (extraHour * (rate * 1.5))
else:
    payment = h * rate
   
print payment
        