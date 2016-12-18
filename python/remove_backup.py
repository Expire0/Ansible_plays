#!/usr/bin/env python2

## Developed by Mas Walls 
## updated 12/18/16
## clean up files  that are more than 5 days old. 
## Test case , create some empty dummy files using touch -d -5days filename

from os import path
from datetime import datetime, timedelta
from os import listdir
from os import remove
from shutil import rmtree
import os

####

def check(dir, idstring, file):
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


def directory():
      for root, dirs, files in os.walk("/home/mas/Documents", topdown=False):
   
          for name in dirs:
              #print(os.path.join(root, name))
              if "test" in name:
                  found =os.path.join(root, name)
                  # print("Found " + found)
                  get = os.path.getmtime(found)
                  get1 = datetime.fromtimestamp(get).strftime('%Y-%m-%d')
                  print("found " + found + "with a timestamp of " + get1)
                  days_ago = datetime.now() - timedelta(days=0)
                  if get1 <  str(days_ago):
                     #rmtree(found)
                     print ("Removing files older then 5 days " + found)


if __name__ == '__main__':

	route = "/home/mas/Documents/"
	days_ago = datetime.now() - timedelta(days=0)
	###logging 
	filename = '/var/log/fileCleanup.log'
	file = open(filename,'a')
	idstring = "test"
#check(route, idstring, file)
#directory()
