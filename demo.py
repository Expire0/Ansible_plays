import ntplib
from time import ctime
import time , calendar , os
import datetime
import dateutil.relativedelta
from subprocess import Popen, PIPE
import sys


#reference points 
#https://stackoverflow.com/questions/12664295/ntp-client-in-python
#https://stackoverflow.com/questions/6574329/how-can-i-produce-a-human-readable-difference-when-subtracting-two-unix-timestam

c = ntplib.NTPClient()
response = c.request('ntp-ch2-1p.sys.comcast.net')
hmm =response.tx_time
#print(hmm[11:-8])
print(hmm)


sub= "@"
sub1 = sub + str(hmm)

hmm2 = calendar.timegm(time.gmtime()) #why use this when you can call time.time() ? --hel

dt1 = datetime.datetime.fromtimestamp(hmm) # 1973-11-29 2i2:33:09
dt2 = datetime.datetime.fromtimestamp(hmm2) # 1977-06-07 23:44:50
rd = dateutil.relativedelta.relativedelta(dt2, dt1)

# 3 years, 6 months, 9 days, 1 hours, 11 minutes and 41 secondsi


mas = rd.minutes

if mas < -1 :
    print(" %d hours, %d minutes and %d seconds" % (rd.hours, rd.minutes, rd.seconds))
    print("Time is out of sync & self correctng ")
    code =Popen(["date", "-s", sub1])   
    code.communicate()

elif mas > 1 :
    print(" %d hours, %d minutes and %d seconds" % (rd.hours, rd.minutes, rd.seconds))
    print("Time is out of sync & self correctng ")
    code =Popen(["date", "-s", sub1])                               
    code.communicate()

else:
    print("Time is within the threshold of one min")
