#!/usr/bin/env python3

###convert unix team to human readable time. This works if the unix time is in milliseconds. 

import datetime 


time = input("Enter the Cyclone event time to be converted: ")

#convert to seconds 
fix = int(time) / 1000

value = datetime.datetime.fromtimestamp(fix)

print(value.strftime('%Y-%m-%d %H:%M:%S'))
