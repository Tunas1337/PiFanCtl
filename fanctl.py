#USB Fan Controller v1.0 - Tunas1337
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import re
import sys

helpArr = ["h", "help", "-h"]

def displayHelp():
    print("")
    print("fanctl <port> <tempTreshold> <pollingtime>")
    print("port - which usb port to use (default: 2)")  
    print("tempThreshold - in celsius, the limit to turn the fan on or off (default: 60)")
    print("pollingTime - in seconds, how many times to check & update the fan (default: 10)")
    print("")
    
def fanOn() :
	os.system("sudo uhubctl -a 1 -p%s -l1-1 >/dev/null 2>&1" % port)

def fanOff() :
	os.system("sudo uhubctl -a 0 -p%s -l1-1 >/dev/null 2>&1" % port)

#Defaults for vars follow below:
tempThreshold = 60 #in Celsius
pollingTime = 10 #in seconds
verbose = True #display temperature every pollingTime seconds
port = 2

#Support for commandline arguments to change vars
if len(sys.argv) == 2:
    if sys.argv[1].lower() in helpArr:
        displayHelp()
        sys.exit()
    else:
        #only the port specfied
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Specified values need to be valid integers")
            displayHelp()
            sys.exit()
elif len(sys.argv) == 3:
    # port and tempThreshold specfied
    try:
        port = int(sys.argv[1])
        tempThreshold = int(sys.argv[2])
    except ValueError:
        print("Specfied values need to be valid integers")
        displayHelp()
        sys.exit()
elif len(sys.argv) == 4:
    # port, tempThreshold and pollingTime specfied
    try:
        port = int(sys.argv[1])
        tempThreshold = int(sys.argv[2])
        pollingTime = int(sys.argv[3])
    except ValueError:
        print("Specfied values need to be valid integers")
        displayHelp()
        sys.excit()
    
print("Starting program... port: %s, tempThreshold: %s, pollingTime: %s" %(port, tempThreshold, pollingTime))
isFanOn = True
while(1):
	temperature = os.popen("sudo cat /sys/class/thermal/thermal_zone0/temp").read();
	temp_decimal = int(temperature) / 1000
	if verbose == True:
		print("Current temperature: " + str(temp_decimal) + "°C")
	if (temp_decimal) >= tempThreshold:
		fanOn()
		isFanOn == True
	else:
		if isFanOn == True:
			fanOff()
			isFanOn == False
	time.sleep(pollingTime)


