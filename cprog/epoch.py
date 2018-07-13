import ntplib
from time import ctime
import time , calendar
import datetime
import dateutil.relativedelta

#reference points 
#https://stackoverflow.com/questions/12664295/ntp-client-in-python
#https://stackoverflow.com/questions/6574329/how-can-i-produce-a-human-readable-difference-when-subtracting-two-unix-timestam

c = ntplib.NTPClient()
response = c.request('ntp-ch2-1p.sys.comcast.net')
hmm =response.tx_time
#print(hmm[11:-8])
print(hmm)

hmm2 = calendar.timegm(time.gmtime()) #why use this when you can call time.time() ? 

dt1 = datetime.datetime.fromtimestamp(hmm) # 1973-11-29 2i2:33:09
dt2 = datetime.datetime.fromtimestamp(hmm2) # 1977-06-07 23:44:50
rd = dateutil.relativedelta.relativedelta(dt2, dt1)

print ("%d years, %d months, %d days, %d hours, %d minutes and %d seconds" % (rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds))
# 3 years, 6 months, 9 days, 1 hours, 11 minutes and 41 seconds
~                                                                 

misc notes 
we will remove the -g option from the ntp config


test case , 

Does NTP stop when the panic threshold is reached and does this log into /var/log/message
Can we 	query the time server directly ? Python maybe?

use python to compare the epoch time to the current epoch time of the system. 


