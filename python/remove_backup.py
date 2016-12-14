#!/usr/bin/env python2

## Developed by Mas Walls 
## updated 12/13/16
## clean up files  that are more than 5 days old. 
## Test case , create some empty dummy files using touch -d -5days filename

from os import path
from datetime import datetime, timedelta
from os import listdir
from os import remove


route = "/var/backup/ldap/"

days_ago = datetime.now() - timedelta(days=5)

###logging 
filename = '/var/backup/scripts/clean.log'
file = open(filename,'a')



####

def check(dir=route, idstring="openldap", file=file):
	check = listdir(dir)
	for i in check:
     		if idstring in i:
         		get = path.getmtime(dir + i)
         		get1 = datetime.fromtimestamp(get).strftime('%Y-%m-%d')
         		if get1 <  str(days_ago):
             			print "Removing files older then 5 days " + i
             			file.write("Removing files older then 5 days " + i + "\n")
             			remove(dir + i)
	file.close()

if __name__ == '__main__':
	check()
