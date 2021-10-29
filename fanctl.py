#USB Fan Controller v1.0 - Tunas1337
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import re
import sys
import argparse

helpArr = ["h", "help", "-h"]

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--port', '-p', type=int, default=2, help="which usb port to use (default: 2)")
arg_parser.add_argument('-v', '--verbose', action="store_true", help="Be verbose (output information every polling cycle to stdout")
arg_parser.add_argument('--temp', '-t', type=int, default=60, help="in celsius, the limit to turn the fan on or off (default: 60)")
arg_parser.add_argument('--polling_time', '-u', type=int, default=10, help="in seconds, how many times to check & update the fan (default: 10)")
args = arg_parser.parse_args()
    
def fanOn() :
	os.system("sudo uhubctl -a 1 -p%s -l1-1 >/dev/null 2>&1" % args.port)

def fanOff() :
	os.system("sudo uhubctl -a 0 -p%s -l1-1 >/dev/null 2>&1" % args.port)

print("Starting program... port: %s, temp threshold: %s, polling time: %s" %(args.port, args.temp, args.polling_time))
isFanOn = True
while(1):
	temperature = os.popen("sudo cat /sys/class/thermal/thermal_zone0/temp").read();
	temp_decimal = int(temperature) / 1000
	if args.verbose == True:
		print("Current temperature: " + str(temp_decimal) + "°C")
	if (temp_decimal) >= args.temp:
		fanOn()
		isFanOn == True
	else:
		if isFanOn == True:
			fanOff()
			isFanOn == False
	time.sleep(args.polling_time)


