



### run a backgroup process and send the stout to a file.   Use the file for a status update and delete 


# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 00:07:07 2016

@author: mas
"""

#!/usr/bin/env python3

import subprocess, os , sys

mas = "hmm"
process = "run.sh"

#os.unlink("check")

## run background process

code= subprocess.call(["./run.sh & "],shell=True)


## check if process is running
if 
code= subprocess.call(["tail -f check "],shell=True)

print(mas)
