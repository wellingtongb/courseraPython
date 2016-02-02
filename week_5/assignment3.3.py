score = raw_input("Enter a score between 0.0 and 1.0: ")
try:
	floatScore = float(score)
except Exception, e:
	print("Please you must insert numeric data")
	quit()
   
if(floatScore > 0.9):
	print " A"
elif floatScore > 0.8:
	print " B"
elif floatScore > 0.7:
	print " C"
elif floatScore > 0.6:
	print" D"
else:
	print" F"