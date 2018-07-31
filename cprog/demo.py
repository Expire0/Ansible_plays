from time import ctime
import time , calendar , os, sys, logging, datetime , ntplib
import dateutil.relativedelta
from subprocess import Popen, PIPE


#reference points 
#https://stackoverflow.com/questions/12664295/ntp-client-in-python
#https://stackoverflow.com/questions/6574329/how-can-i-produce-a-human-readable-difference-when-subtracting-two-unix-timestam

c = ntplib.NTPClient()   #create a object of the class 
response = c.request('<server>')
isntp =response.tx_time

sub= "@"
sub1 = sub + str(isntp)

isOS = calendar.timegm(time.gmtime()) #why use this when you can call time.time() ? --hel

dt1 = datetime.datetime.fromtimestamp(isntp) # 1973-11-29 2i2:33:09
dt2 = datetime.datetime.fromtimestamp(isOS) # 1977-06-07 23:44:50
rd = dateutil.relativedelta.relativedelta(dt2, dt1)

# 3 years, 6 months, 9 days, 1 hours, 11 minutes and 41 secondsi

#logging config 

validate = rd.minutes

if validate < -1 :
#    print(" %d hours, %d minutes and %d seconds" % (rd.hours, rd.minutes, rd.seconds))
#    print("Time is out of sync & self correctng ")
    code =Popen(["date", "-s", sub1])   
    code.communicate()
    logging.basicConfig(format='%(asctime)s %(message)s',filename='clocksync-natprov.log',level=logging.INFO)
    logging.info('The clock was out of sync with the NTP server by -%s minutes ' , validate)

elif validate > 1 :
#    print(" %d hours, %d minutes and %d seconds" % (rd.hours, rd.minutes, rd.seconds))
#    print("Time is out of sync & self correctng ")
    log = rd
    code =Popen(["date", "-s", sub1])                               
    code.communicate()
    logging.basicConfig(format='%(asctime)s %(message)s',filename='clocksync-natprov.log',level=logging.INFO)
    logging.info('The clock was out of sync with the NTP server by %s minutes' , validate)
else:
    print("Time is synced")
