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
   # print("check complete")
#is_running(b"run.sh")
