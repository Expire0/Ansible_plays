#!/opt/comcast/interpreters/python-3.3.2/bin/python3.3


from time import ctime
import time , calendar , os, sys, logging, datetime 
from  clock_lib.dateutil import relativedelta 
from clock_lib import ntplib
from subprocess import Popen, PIPE


def test():
    c = ntplib.NTPClient()    
    response = c.request('ntp-ch2-1p.sys.comcast.net')
    isntp =response.tx_time

    sub= "@"
    sub1 = sub + str(isntp)

    isOS = calendar.timegm(time.gmtime()) 

    dt1 = datetime.datetime.fromtimestamp(isntp) 
    dt2 = datetime.datetime.fromtimestamp(isOS) 
    rd = relativedelta.relativedelta(dt2, dt1)


    #logging config 

    validate = rd.minutes

    if validate < -1 :
        code =Popen(["date", "-s", sub1])   
        code.communicate()
        logging.basicConfig(format='%(asctime)s %(message)s',filename='clocksync-natprov.log',level=logging.INFO)
        logging.info('The clock was out of sync with the NTP server by -%s minutes ' , validate)

    elif validate > 1 :
        log = rd
        code =Popen(["date", "-s", sub1])                               
        code.communicate()
        logging.basicConfig(format='%(asctime)s %(message)s',filename='clocksync-natprov.log',level=logging.INFO)
        logging.info('The clock was out of sync with the NTP server by %s minutes' , validate)
    else:
        print("Time is synced")
