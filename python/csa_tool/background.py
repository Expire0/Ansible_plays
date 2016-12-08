###   check for running process

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 00:07:07 2016
@author: mas
"""

#!/usr/bin/env python3

import re
import subprocess

check="./run.sh"

def is_running(process):

    s = subprocess.Popen(["ps", "axw"],stdout=subprocess.PIPE)
    for x in s.stdout:
        if process in x:
            print("Processing is running")
           # print(x)
        #else:
         #   print("no")
    print("check complete")
is_running(b"run.sh")

##############



sample run command 

#!/usr/bin/bash

mas=0
run='/usr/bin/date'

rm -rf check
while [ $mas -lt 10 ] ; do
       $run >> check  
       sleep 5
done

###
python 

### run a backgroup process and send the stout to a file.   Use the file for a status update and delete 
### http://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call

#!/usr/bin/env python3

import subprocess, os , sys

mas = "hmm"
process = "run.sh"

#os.unlink("check")

## run background process

code= subprocess.call(["./run.sh & "],shell=True)


## check if process is running
#code= subprocess.call(["tail -f check "],shell=True)

print(mas)



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
