#inches to feet converter
#units enters a measurement to be converted in inches
units = input('Enter measurement in inches:')
#while the user provides new measurements
while (units != "stop"):
#the measurement in inches are converted to feet and the string into an integer
    newUnits = int(units)/12
    print(newUnits, "ft")
#user enters another measurement in inches or enters stop
    units = input('Enter measurement in inches:')
