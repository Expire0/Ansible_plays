#!/usr/bin/env python2

## Developed by Mas Walls 
## updated 12/13/16
## clean up files  that are more than 5 days old. 

from os import path
from datetime import datetime, timedelta
from os import listdir
from os import remove

check = listdir("/var/backup/ldap/")
route = "/var/backup/ldap/"

days_ago = datetime.now() - timedelta(days=5)

###logging 
file = open('/var/backup/scripts/clean.log','a')



####


for i in check:
     if "openldap" in i:
         get = path.getmtime(route + i)
         get1 = datetime.fromtimestamp(get).strftime('%Y-%m-%d')
         if get1 <  str(days_ago):
             print "Removing files older then 5 days " + i
             file.write("Removing files older then 5 days " + i + "\n")
             remove(route + i)
file.close()
