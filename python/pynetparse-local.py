#!/usr/bin/env python
from netaddr import *
import os
import subprocess
#tool requires netaddr module 

scope = raw_input("which scope do you want to expand?  " )
pg = raw_input("which primary dhcp:  ")
pgs = pg.replace("pdhcp", "sdhcp")
force = IPNetwork(scope)
all= list(force)
CNRUS = raw_input("CNR Username: ")
CNRPA = raw_input("CNR Password: ")


def dipps():
    global ccm
    global CNRUS
    global CNRPA
    for ccm in all:
	   # CNRUS = raw_input("CNR Username: ")
	    #CNRPA = raw_input("CNR Password: ")
	    ccm = str(ccm)
            print "nrcmd -C " + pg + " -N " + CNRUS + " -P " + CNRPA +" lease " + ccm + " force-available "
	  
	   # print "nrcmd -C " + pg + " lease " + ccm + " force-available "
           # subprocess.call(output, shell=True)
def dippss():

    for ccm in all:
	     ccms = str(ccm)
	     print "nrcmd -C " + pgs + " -N " + CNRUS + " -P " + CNRPA +" lease " + ccms + " force-available "

	    # print "nrcmd -C " + pgs + " lease " + ccms + " force-available "
            # subprocess.call(output, shell=True)
dipps()
print "\n"
dippss()
