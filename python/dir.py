# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:19:14 2016

@author: mas
"""

# !/usr/bin/python

from datetime import datetime,timedelta
import os
from shutil import rmtree
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