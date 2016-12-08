### run a backgroup process and send the stout to a file.   Use the file for a status update and delete 
### http://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call

#!/usr/bin/env python3

from subprocess import Popen, PIPE
import sys
from check_background import is_running

mas = "hmm"
process = "run.sh"

#os.unlink("check")

## run background process

code= Popen(['./run.sh','&'],stdout=PIPE, stderr=PIPE)
while True:
    line = code.stdout.readline().decode('utf-8')
    if "log" in line:
        print("Batch received\n")
        print("Your log file is " + line)
    break

## check if process is running
#code= subprocess.call(["tail -f check "],shell=True)

is_running(b"run.sh")