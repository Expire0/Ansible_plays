
##### list log files and output 
### To do  run a process and grab the standout when running the apiscripter we will need the log number ###
##then use this log number to locate the log files and output the contents ###

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 04:36:15 2016

@author: mas
"""

import os 


p = os.listdir('/var/log/')


for i in p:
    if 'Xorg' in i:
        print(i)