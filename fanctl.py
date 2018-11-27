#!/usr/bin/python3
import os
import time
import re

#USB Fan Controller v1.0 - Tunas1337
#Change the -p parameter in fanOn() and fanOff() to reflect the port your fan is plugged into!
#Other settable vars follow below:
tempThreshold = 60 #in Celsius
pollingTime = 10 #in seconds

def fanOn() :
	os.system("sudo uhubctl -a 1 -p2 -l1-1 >/dev/null 2>&1")

def fanOff() :
	os.system("sudo uhubctl -a 0 -p2 -l1-1 >/dev/null 2>&1")

#original code to test fan on/off
'''print("Testing subsystem...")
os.system("sudo uhubctl -a 0 -p2 -l1-1")
time.sleep(3)
os.system("sudo uhubctl -a 1 -p2 -l1-1")
print("Test successful.")'''

print("Starting program...")
isFanOn = True
while(1):
	temperature = os.popen("sudo cat /sys/class/thermal/thermal_zone0/temp").read();
	temp_decimal = int(temperature) / 1000
	print("Current temperature: " + str(temp_decimal) + "°C")
	if (temp_decimal) >= tempThreshold:
		fanOn()
		isFanOn == True
	else:
		if isFanOn == True:
			fanOff()
			isFanOn == False
	time.sleep(pollingTime)


