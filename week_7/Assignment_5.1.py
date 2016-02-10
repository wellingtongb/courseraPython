largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break    #checking if user wants finish insertion
    if len(num) < 1 : break     #checking if user insert nothing
    try:
        numInt = int(num)
        if largest is None or numInt > largest:
            largest = numInt
        if smallest is None or numInt < smallest:
            smallest = numInt
    except:
        print "Invalid input"
    continue                #If user insert a garbage input, returns to input command

print "Maximum is", largest
print "Minimum is", smallest